#! /usr/bin/env python

"List Teradata objects with Linux commands ls/find like options"

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

import sys

from .util import Listing
from .util import Col
from tdtypes import DBObjPat

class TVM(Listing):
	"TVM listing"

	def user_args(self):

		yield lambda p: p.add_argument("names", metavar='OBJECT', nargs='*', type=DBObjPat, help=DBObjPat.__doc__)
		yield args_filter
		yield args_display
		yield args_order

	def all_cols(self, opts):
		# pylint: disable=locally-disabled, bad-whitespace
		return [
		  Col('TableKind',    "T",       1)
		, Col("CreatorName",  "Creator", 1)

		, Col(opts.sizecol,   "Size_",   1)
		, Col("TableSkew",    "Skew%",   1)

		, Col(opts.timecol,   "Created" if opts.timecol == 'CreateTimestamp' else 'Altered', 1)

		, Col("T.DatabaseName || '.' || T.TableName" if opts.showdb else 'T.TableName', "Table", 0)
		]


	def build_sql(self, names, cols, opts):
		from .. import vsch

		# pylint: disable=locally-disabled, bad-whitespace
		where = []
		if names:
			pred = '\n    OR  '.join(n.search_cond('T.DatabaseName', 'T.TableName') for n in names)
			where.append(pred if len(names) == 1 else '('+pred+')')
		else:
			where.append('T.DatabaseName = Database')

		if opts.type:
			where.append("Position(TableKind In '{}') > 0".format(opts.type))
		if opts.hide:
			where.extend("NOT ({})".format(p.search_cond(db='T.DatabaseName', tb='T.TableName')) for p in opts.hide)
		if opts.ctime:
			where.append('CAST(T.CreateTimestamp AS DATE) {}'.format(opts.ctime))
		if opts.mtime:
			where.append('CAST(T.LastAlterTimestamp AS DATE) {}'.format(opts.mtime))
		if opts.user:
			where.append("T.CreatorName = '{}'".format(opts.user))
		if opts.size:
			where.append("{} {}".format(opts.sizecol, opts.size))
		if opts.skew:
			where.append("TableSkew {}".format(opts.skew))

		sql = """\
SELECT {}
  FROM {dbc.TablesV} T
  LEFT JOIN (
        SELECT DatabaseName
             , TableName
             , SUM(CurrentPerm) AS TableSize
             , MAX(CurrentPerm) * COUNT(*) AS ImpactSize
			 , CAST((1.0 - AVG(CurrentPerm) / NULLIFZERO(MAX(CurrentPerm))) AS DECIMAL(4,3)) AS TableSkew
          FROM {dbc.TableSizeV} Z
         GROUP BY 1,2
       ) Z ON Z.DatabaseName = T.DatabaseName AND Z.TableName = T.TableName
 WHERE {}""".format('\n     , '.join(cols), '\n   AND '.join(where), dbc=vsch.load_schema('dbc'))

		order = []
		if opts.group:
			order.append('TableKind')
		if opts.sort:
			if opts.sort == 'name' and opts.showdb:
				order.append('T.DatabaseName')
			order.append({'size': 'Size_', 'name':'T.TableName', 'time':opts.timecol, 'mtime':'LastAlterTimestamp'}[opts.sort])

		if order:
			def collate(c):
				"generate correct SQL ORDER BY clause"
				desc = c in ['Size_', opts.timecol, 'LastAlterTimestamp']
				if opts.reverse and c != 'TableKind':
					desc = not desc
				return ' DESC' if desc else ''

			sql += "\n ORDER BY " + ', '.join(["{}{}".format(c, collate(c)) for c in order])

		return sql


def main():
	"script entry-point"
	return TVM(__name__, __doc__).ls()


def args_filter(p):
	"options to filter listing"
	import os.path

	class rel_time:
		"relative time like in find linux command"
		def __init__(self, val):
			self.val = abs(int(val))
			self.op = {'+': '<', '-': '>'}.get(val[0], '=')

		def __str__(self):
			import datetime as dt
			return "{} '{:%Y-%m-%d}'".format(self.op, dt.date.today() - dt.timedelta(days=self.val))

	class rel_size:
		"relative size like in find linux command"
		exps = {'p': '15', 't': '12', 'g': '9', 'm': '6', 'k': '3'}
		def __init__(self, val: str):
			self.op = '<' if val[0] == '-' else '>='
			if val[-1].lower() in self.exps:
				self.val = '{}e{}'.format(abs(int(float(val[:-1]))), self.exps[val[-1]])
			else:
				self.val = str(abs(int(float(val))))

		def __str__(self):
			return self.op + ' ' + self.val

	class rel_pct:
		"relative skew type"
		def __init__(self, val:str):
			self.op = '<' if val[0] == '-' else '>='
			self.val = abs(float(val))
			if self.val > 1:
				raise ValueError("Skew must be a fraction between -1.0..+1.0")

		def __str__(self):
			return "{} {}".format(self.op, self.val)

	cmd = os.path.split(sys.argv[0])[1]
	kind = {'lstb':'TO', 'lsvw':'V', 'lspr':'PE', 'lsji':'I', 'lsmc':'M', 'lsfn':'ABCFRSL'}.get(cmd)

	# pylint: disable=locally-disabled, bad-whitespace
	g = p.add_argument_group("Filters")
	g.add_argument(      "--type",    type=str.upper,    default=kind,     help="only include TVM entries with specified TableKind")
	g.add_argument("-I", "--hide",    type=DBObjPat,     action='append', metavar='PATTERN',  help="do not list implied entries matching PATTERN")
	g.add_argument(      "--mtime",   metavar='+N,-N,N', type=rel_time,    help="modify time n*24 hours ago")
	g.add_argument(      "--ctime",   metavar='+N,-N,N', type=rel_time,    help="create time n*24 hours ago")
	g.add_argument(      "--size",    metavar='+N,-N,N', type=rel_size,    help="size more/less than specified")
	g.add_argument(      "--skew",    metavar='+N,-N,N', type=rel_pct,     help="skew more/less than specified")
	g.add_argument(      "--user",                                         help="only display tables created by this user")

def args_display(p):
	"options to format the display"
	g = p.add_argument_group("Display")

	# pylint: disable=locally-disabled, bad-whitespace
	g.add_argument("-D", dest="showdb", action="store_false", help="show just the object name without database prefix")
	g.add_argument("-i", "--impact", dest="sizecol", action='store_const', const='ImpactSize', default='TableSize', help="report impact size")
	g.add_argument("-c", dest='timecol', action="store_const", default='LastAlterTimestamp', const='CreateTimestamp',
		help="use create instead of modified time for display/sort")

	from .util import args_size
	args_size(g)

def args_order(p):
	"options to order the listing"
	from .util import args_sort
	g = p.add_argument_group("Ordering")
	g.add_argument("--group", action="store_true", help="group by object type")
	args_sort(g)


if __name__ == '__main__':
	sys.exit(main())
