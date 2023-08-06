#! /usr/bin/env python
# -*- coding: utf8 -*-

"Print concise Teradata explain plan report"

from tdtools import util
from yappt import tabulate, treeiter
from tdtypes import sqlcsr

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2017, Paresh Adhia"
__license__ = "GPL"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

logger = util.getLogger(__name__)

class Err(Exception):
	"script defined error"

class TableLike:
	"A database object that stores data, optionally built using one or more children"
	def __init__(self):
		self.parent, self.children = None, []

class TV(TableLike):
	"A permanent database data object"
	def __init__(self, sch, name, rows=None):
		super().__init__()
		self.sch, self.name, self.rows, self.lock = sch, name, int(rows) if rows else None, None

	def __str__(self):
		return self.sch + "." + self.name

class Table(TV):
	"Tag class for a database table"

class View(TV):
	"Tag class for a database view"

class Spool(TableLike):
	"A temporary object that stores intermediate results of an intermediate database operation"
	maxdigits = 1

	def __init__(self, num, conf=None, rows=None):
		super().__init__()
		self.num, self.conf, self.rows, self.step = int(num), conf, int(rows) if rows != None else None, None
		Spool.maxdigits = max(Spool.maxdigits, len(str(self.num)))

	def __str__(self):
		return 'Spool#{:0{dig}}'.format(self.num, dig=self.maxdigits)

class InList(TableLike):
	"A literal list of values represented as table"
	def __init__(self, numvals):
		super().__init__()
		self.numvals = numvals

	def __str__(self):
		return 'InList[{}]'.format(self.numvals)


class Index:
	def __init__(self, xe):
		self.num = xe.attrib['IndexNum']
		self.uniq = xe.attrib.get('UniqueFlag', 'false') == 'true'
		self.type = {
			"Hash Ordered Secondary Covering": 'HI-Cover',
			"Primary Key": 'PKey',
			"Value Ordered Secondary": 'VOSI',
			"Nonpartitioned Primary": 'PI',
			"Partitioned Primary": 'PPI',
			"Secondary": 'SI',
			"Unique Constraint": 'Uniq',
			"Value Ordered Secondary Covering": 'VOSI-Cover',
			"Spatial": 'Spatial'}[xe.attrib['IndexType']]

	def __str__(self):
		return self.type


class Lock:
	def __init__(self, objx, severity, level):
		self.severity = severity
		self.level = level
		if objx.tag == 'RelationRef':
			self.obj = objlist[objx.attrib['Ref']]
			self.obj.lock = severity
		else:
			raise Err('{0} is unknown tag for locking'.format(objx.tag))

	def __str__(self):
		return '{0}:{1}:{2}'.format(self.obj, self.level, self.severity)


class Source:
	"Represents input to a database step"
	def __init__(self, xe):
		self.pos = int(xe.attrib['AccessPosition'])
		self.obj = self.parts = self.pred = self.IX = None

		for c in xe:
			if   c.tag == 'SpoolRef':    self.obj   = objlist[c.attrib['Ref']]
			elif c.tag == 'RelationRef': self.obj   = objlist[c.attrib['Ref']]
			elif c.tag == 'IndexRef':    self.IX    = objlist[c.attrib['Ref']]
			elif c.tag == 'IN-List':     self.obj   = InList(c.attrib['NumValues'])
			elif c.tag == 'PPIAccess':   self.parts = int(c.attrib['TotalParts'])
			elif c.tag == 'Predicate':   self.pred  = c.attrib['PredicateKind']

	def __str__(self):
		s = str(self.obj)
		if self.IX:
			s += ':'+str(self.IX)
		if self.parts:
			s += '[{}]'.format(self.parts)
		if self.pred:
			s += ':' + self.pred
		return s


class Target:
	"Represents output of a database step"
	def __init__(self, xe):
		geo = xe.attrib.get('GeogInfo','')
		self.geo = {'Duplicated': 'Dupl', 'Hash Distributed': 'Redist'}.get(geo, geo)
		self.sort = None
		for c in xe:
			if   c.tag == 'SpoolRef':    self.obj = objlist[c.attrib['Ref']]
			elif c.tag == 'RelationRef': self.obj = objlist[c.attrib['Ref']]
			elif c.tag == 'SortKey':     self.sort = c.attrib['SortKind']

	def __str__(self):
		return self.geo


class Step:
	"An individual step in database query plan"
	def __init__(self, xe):
		self.num = int(xe.attrib['StepLev1Num'])
		self._op = xe.find('StepDetails')[0].tag if xe.find('StepDetails') != None else xe.attrib['QCFStepKind']
		self.num += int(xe.attrib['StepLev2Num']) / 100.0 if xe.attrib['QCFParallelKind'] != 'Sequential' else 0

		self.amps = self.rows = self.time = self.tgt = self.pred = None
		self.src = []

		for c in xe:
			if   c.tag == 'AmpStepUsage': self.amps = c.attrib['QCFAmpUsage']
			elif c.tag == 'SourceAccess': self.src.append(Source(c))
			elif c.tag == 'TargetStore':  self.tgt = Target(c)
			elif c.tag == 'Predicate':    self.pred = c.attrib['PredicateKind']
			elif c.tag == 'OptStepEst':
				if c.attrib.get('EstRowCount'): self.rows = int(c.attrib['EstRowCount'])
				if c.attrib.get('EstProcTime'): self.time = float(c.attrib['EstProcTime'])

		self.src.sort(key=lambda s: s.pos)

		if self.tgt:
			self.tgt.obj.step = self
			self.tgt.obj.children.extend([s.obj for s in self.src])
			for s in self.src:
				s.obj.parent = self.tgt.obj

	@property
	def op(self):
		return self._op + (', '+self.pred if self.pred else '')

	def operands(self):
		return '[{}] -> {}'.format(', '.join([str(s) for s in self.src]), self.tgt or 'Dispatcher') if self.src != None else ''

	def __str__(self):
		stepnum = 'Step#' + ('{0:02d}   '.format(self.num) if int(self.num) == self.num else '{0:05.2f}'.format(self.num))
		return '{0} {1:6} {2}'.format(stepnum, self.op, self.operands())

	@staticmethod
	def fromxml(xe):
		detail = xe.find('StepDetails')
		kind = xe.attrib['QCFStepKind']

		if detail == None:
			StepType =  {'SR': SpoolStep}.get(kind, Step)
		else:
			StepType = {'JIN':JoinStep, 'MLK':LockStep, 'SUM':SumStep}.get(detail[0].tag, Step)

		return StepType(xe)

class SpoolStep(Step):
	@property
	def op(self):
		if self.pred: return self.pred
		if self.tgt == None: return 'Return'
		return self.tgt.geo

class SumStep(Step):
	@property
	def op(self):
		return 'Sum'

class JoinStep(Step):
	def __init__(self, xe):
		super().__init__(xe)

		detail = xe.find('StepDetails/JIN')
		self.jtyp, self.jkind = detail.attrib['JoinType'], detail.attrib['JoinKind']

		# Make Join Kind less verbose
		for word, abbr in {' Join':'-J', 'Product':'Prod', 'Inclusion':'Incl', 'Exclusion':'Excl', 'Dynamic':'Dyn', 'Correlated':'Corr'}.items():
			if word in self.jkind:
				self.jkind = self.jkind.replace(word, abbr)

	@property
	def op(self):
		return self.jkind

class LockStep(Step):
	def __init__(self, xe):
		super().__init__(xe)
		self.locks = []

		for l in xe.findall('StepDetails/MLK/LockOperation'):
			for t in l:
				self.locks.append(Lock(t, l.attrib['LockSeverity'], l.attrib['LockLevel']))

	@property
	def op(self):
		return 'Lock'


def main():
	import xml.etree.ElementTree as et
	global objlist

	args = getargs()

	if args.query:
		xml = query_plan(args.inp, args)
	else:
		try:
			with open(args.inp, 'r') as f:
				doc = f.read()
		except IOError:
			logger.error('Could not open [{}] for reading'.format(args.inp))
			return 1

		if args.xml:
			import re
			xml = re.sub('xmlns=".*?"', '', re.sub('encoding="UTF-16"', 'encoding="utf-8"', doc, 1, flags=re.IGNORECASE), 1)
		else:
			xml = query_plan(doc, args)

	root = et.fromstring(xml)
	objlist = parse_objs(root)
	steps = [Step.fromxml(e) for e in root.findall('Query/Plan/*')]

	print_steps(steps)
	print()
	expl_tree()
	print()

	if args.tb_summary:
		tbls = sorted([(tb.name, tb.sch, tb.rows, tb.lock) for tb in objlist.values() if isinstance(tb, Table)], key=lambda t:t[:2])
		spools = sorted([(str(s), None, s.rows, None) for s in objlist.values() if isinstance(s, Spool)])
		print(tabulate(tbls+spools, columns=['Table', 'Database', 'Rows', 'Lock']))


def getargs():
	from argparse import ArgumentParser

	p = ArgumentParser(description=__doc__)

	p.add_argument("inp", help="Input to the program. Defaul is name sql file")

	g = p.add_mutually_exclusive_group()
	g.add_argument("-x", "--xml", action='store_true', help="Input is XML text instead of SQL query")
	g.add_argument("-q", "--query", action='store_true', help='Input is a query')

	p.add_argument("--tb-summary", action='store_true', help='Print table/spool cardinality summary')

	sqlcsr.dbconn_args(p)

	return p.parse_args()

def query_plan(sql, args):
	with sqlcsr.cursor(args) as csr:
		csr.execute('EXPLAIN IN XML NODDLTEXT '+sql)
		return csr.fetchxml()

def parse_objs(plan):
	objlist = {}
	dblist = {}

	for db in plan.findall('Query/ObjectDefs/*'):
		dblist[db.attrib['Id']] = db.attrib['DatabaseName']
		for tb in db:
			if   tb.tag == 'Relation': objlist[tb.attrib['Id']] = Table(dblist[tb.attrib['DatabaseId']], tb.attrib['TableName'], tb.attrib['Cardinality'])
			elif tb.tag == 'View':     objlist[tb.attrib['Id']] = View(dblist[tb.attrib['DatabaseId']], tb.attrib['ViewName'])
			elif tb.tag == 'Spool':    objlist[tb.attrib['Id']] = Spool(tb.attrib['SpoolNumber'], tb.attrib.get('Confidence'), tb.attrib.get('Cardinality'))
			else:
				raise Err('Unknown Database Object (%s)' % tb.tag)
			for ix in tb:
				if ix.tag == 'Index':
					objlist[ix.attrib['Id']] = Index(ix)

	return objlist

def print_steps(steps):
	def rows():
		for s in steps:
			op   = s.op
			tgt  = '{}, {}'.format(s.tgt.obj,s.tgt) if s.tgt else ''
			src1 = str(s.src[0]) if s.src else ''
			src2 = str(s.src[1]) if len(s.src) > 1 else ''

			yield [s.num, op, tgt, src1, src2]

	print(tabulate(rows(), columns=[('Step', str), 'Operation', 'Target', 'Source 1', 'Source 2']))


def expl_tree():
	def rows():
		for tb in [tb for tb in objlist.values() if isinstance(tb, TableLike) and tb.parent is None]:
			for pfx, ch in treeiter(tb):
				node = str(pfx) + str(ch)
				rows = time = None
				if isinstance(ch, Spool) and ch.step:
					node += ' ({step.op}, {step.tgt.geo} @{step.num})'.format(step=ch.step)
					if ch.step.rows:
						rows, time = ch.step.rows, ch.step.time
				elif isinstance(ch, Table) and ch.rows:
					rows = ch.rows

				yield node, rows, time

	print(tabulate(rows()))


if __name__ == '__main__':
	import sys
	sys.exit(main())
