#! /usr/bin/env python
# -*- coding: utf8 -*-
"List Teradata Database hierarcy"

from lazy import lazy
from tdtypes import sqlcsr
from . import util
from . import vsch

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016, Paresh Adhia"
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

class Dbase:
	"A Teradata database, has attributes and may own other databases"
	def __init__(self, name, alloc=0, used=0, impact=0, peak=0):
		self.name, self.alloc, self.used, self.impact, self.peak = name, alloc, used, impact, peak
		self.owns = []

	@lazy
	def alloc_rup(self):
		"allocated size, rolled up"
		return self.alloc + sum([c.alloc_rup for c in self.owns])

	@lazy
	def used_rup(self):
		"used size, rolled up"
		return self.used + sum([c.used_rup for c in self.owns])

	@lazy
	def impact_rup(self):
		"impact size, rolled up"
		return self.impact + sum([c.impact_rup for c in self.owns])

	@lazy
	def peak_rup(self):
		"peak size, rolled up"
		return self.peak + sum([c.peak_rup for c in self.owns])

	def __str__(self):
		return self.name

def main():
	"script entry-point"
	args = user_args()

	sql = build_sql(
		args.seed,
		reverse=args.ancestors,
		get_sizes=args.details > 0,
		max_depth=args.max_depth,
		dbkind=args.dbkind,
		non_zero=args.non_zero
	)

	if args.sql:
		print(sql.replace('\t', '    ')+';')
	else:
		logger.info('SQL: %s', sql)
		with sqlcsr.cursor(args) as csr:
			tree = build_tree(csr.execute(sql) if args.sizefmt else [(d, l, 0, 0, 0) for d, l in csr.fetchall()])
		if tree:
			print_tree(tree, details=args.details, sizefmt=args.sizefmt, rollup=args.cumulative)

def build_sql(root, reverse=False, get_sizes=False, max_depth=None, dbkind=None, non_zero=False):
	"return a recurisvely sql that returns either ancestors or descendants from root"
	dbc = vsch.load_schema('dbc')
	P, C = ('C', 'P') if reverse else ('P', 'C') # print top-down or reverse (bottom-up) hierarchy

	cond = ['c.CDB is not null', 'p.DB = c.PDB']
	if max_depth:
		cond.append("Depth < {}".format(max_depth))
	if dbkind:
		cond.append("DBKind = '{}'".format(dbkind))
	if non_zero:
		cond.append("PermSpace > 0")
	where = "\n       and ".join(cond)

	return f"""\
with incl_sizes as (
	select DBPath
		, DB
		, Depth
		, AllocSize
		, UsedSize
		, ImpactSize
		, PeakSize
	from hierarchy h
	join sizes z on z.DatabaseName = h.DB
),
excl_sizes as (
	select DBPath
		, DB
		, Depth
		, AllocSize
		, 0 AS UsedSize
		, 0 AS ImpactSize
		, 0 AS PeakSize
	from hierarchy h
),
recursive hierarchy(DB, DBPath, Depth, AllocSize) as (
	select DB
		, cast(DB as varchar(30000))
		, 0
		, PermSpace
	from ancestry s
	where DB = '{root}'

	union all

	select c.CDB
		, DBPath || ':' || CDB
		, Depth + 1
		, c.PermSpace
	from ancestry c,
		hierarchy p
	where {where}
),
ancestry as (
	select DatabaseName         as DB
		, DatabaseName          as {C}DB
		, case when DatabaseName = 'DBC' then NULL else OwnerName end  as {P}DB
		, PermSpace
		, DBKind
	from {dbc.DatabasesV}
),
sizes as (
	select DatabaseName
		, SUM(CurrentPerm) As UsedSize
		, MAX(CurrentPerm) * COUNT(*) As ImpactSize
		, SUM(PeakPerm)    As PeakSize
	from {dbc.DiskSpaceV}
	group by 1
)
select Depth
	, DB
	, AllocSize
	, UsedSize
	, ImpactSize
	, PeakSize
from {'incl' if get_sizes else 'excl'}_sizes
order by DBPath"""

def build_tree(dbinfo):
	"build bierarchical tree using the depth information and return root element"

	unget = False

	def dbgen():
		"database generator with ability to unget"
		nonlocal unget

		for (level, name, alloc, used, impact, peak) in dbinfo:
			db = Dbase(name, alloc, used, impact, peak)
			yield (level, db)
			while unget:
				unget = False
				yield (level, db)

	iterdb = dbgen()

	def db_for_level(level, dblist):
		"Get all databases for given level"
		nonlocal unget

		for new_level, db in iterdb:
			if new_level > level:
				dblist[-1].owns.extend(db_for_level(new_level, [db]))
			elif new_level == level:
				dblist.append(db)
			else:
				unget = True
				return dblist
		return dblist

	return next(iter(db_for_level(0, [])), None)

def print_tree(tree, details=0, sizefmt=None, rollup=False):
	"print databses hierarchically, with optional information if requested"
	from yappt import treeiter, PPCol, HumanInt, formatted

	def row0(name, a, i, u, p):
		return (name,)
	def row1(name, a, i, u, p):
		return (name, HumanInt(a), HumanInt(a-i), HumanInt(u), (u/a if a > 0 else None))
	def row2(name, a, i, u, p):
		return (*row1(name, a, i, u, p), HumanInt(i), (i - u) / i if i > 0 else None)

	data = ((pfx, db) for pfx, db in treeiter(tree, getch=lambda d: d.owns))
	if rollup:
		data = ((f"{pfx}{db}", db.alloc_rup, db.impact_rup, db.used_rup, db.peak_rup) for pfx, db in data)
	else:
		data = ((f"{pfx}{db}", db.alloc, db.impact, db.used, db.peak) for pfx, db in data)

	if details == 0:
		data = (row0(*row) for row in data)
	else:
		SizeCol = lambda c: PPCol(c, ctype=HumanInt, fmtval=lambda v: format(v, sizefmt))
		PctCol = lambda c: PPCol(c, ctype=float, fmtval=lambda v: format(v, '.0%'))

		cols = ['Database', SizeCol('Alloc'), SizeCol('Free'), SizeCol('Used'), PctCol('%')]
		if details == 1:
			data = formatted((row1(*row) for row in data), columns=cols)
		else:
			cols = cols + [SizeCol('Skewed'), PctCol('%')]
			data = formatted((row2(*row) for row in data), columns=cols)

	for row in data:
		print(' '.join(row))

def user_args():
	"run-time script options"
	from argparse import ArgumentParser

	p = ArgumentParser(description=__doc__, add_help=False)

	p.add_argument("seed", metavar='DB', nargs='?', default='dbc', help="database at the root of the hierarchy (default DBC)")
	p.add_argument('--help', action='help', help='show this help message and exit')
	p.add_argument("-a", "--ancestors", action='store_true', help="show ancestors instead of descendents")

	x = p.add_mutually_exclusive_group()
	x.add_argument("--free", dest='size2', action="store_const", const='free', default='used', help="likewise, but show free instead of used space")
	x.add_argument("--peak", dest='size2', action="store_const", const='peak', help="likewise, but show peak instead of used space")

	p.add_argument("--skew", action="store_true", help="Factor in Skew when calculating sizes")
	p.add_argument("-c", "--cumulative", action='store_true', help="list cumulative size that includes size of *non-filtered* child databases")

	p.add_argument("-l", dest='details', default=0, action='count', help="long list -- show allocated and used database sizes")
	g = p.add_mutually_exclusive_group()
	g.add_argument("-h", "--human-readable", dest='sizefmt', action="store_const", const='.1h', default=',d',
		help="with -l, print human readable sizes (e.g., 1K 234M 2G)")
	g.add_argument("--si", dest='sizefmt', action="store_const", const='.1s', help="likewise, but use powers of 1000 not 1024")

	g = p.add_argument_group("Filters")
	g.add_argument("--max-depth", metavar='INT', type=int, help="limit hierarchy depth to the specified value")
	g.add_argument("-Z", "--non-zero", action='store_true', help="only show databases with non-zero PERM space")
	x = g.add_mutually_exclusive_group()
	x.add_argument('-d', '--only-db', dest='dbkind', action='store_const', const='D', help='list only databases')
	x.add_argument('-u', '--only-users', dest='dbkind', action='store_const', const='U', help='list only users')

	p.add_argument("--sql", action='store_true', help="show generated SQL; do not run it")

	sqlcsr.dbconn_args(p)

	return p.parse_args()

if __name__ == '__main__':
	import sys
	sys.exit(main())
