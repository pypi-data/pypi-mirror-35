#! /usr/bin/env python

"List Teradata Databases"

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

import tdtypes as td

from .util import Listing
from .util import Col

class Database(Listing):
	"Database listing"

	def user_args(self):
		yield lambda p: p.add_argument("names", metavar='DB', nargs='*', help="search for only specific names (wild-cards allowed)")
		yield args_filter
		yield args_display
		yield args_order

	def all_cols(self, opts):
		# pylint: disable=locally-disabled, bad-whitespace
		return [
			  Col("d.DBKind",        "T",       1)

			, Col("PermSpace",       "Alloc_",  1)
			, Col("CurrPerm",        "Used_",   2)
			, Col("ImpactPerm",      "Impact_", 2)
			, Col("PermSpace - ImpactPerm", "Free_", 2)
			, Col("UsedPct",         "Used%",   1)
			, Col("DBSkew",          "Skew%",   2)

			, Col("d.DatabaseName",  "DB",      0)

			, Col("OwnerName",       "Owner",   2)
			, Col("CreateTimestamp", "Created", 2)
			, Col("CreatorName",     "Creator", 2)
		]

	def build_sql(self, names, cols, opts):
		from .. import vsch

		sql = """\
SELECT {}
FROM {dbc.DatabasesV} d
LEFT JOIN (
	SELECT DatabaseName
		, Sum(CurrentPerm) as CurrPerm
		, CAST(Sum(CurrentPerm) as FLOAT) / NullIFZero(Sum(MaxPerm)) as UsedPct
		, CAST((1.0 - AVG(CurrentPerm) / NULLIFZERO(MAX(CurrentPerm))) AS DECIMAL(4,3)) AS DBSkew
		, Max(CurrentPerm) * count(*) as ImpactPerm
	FROM {dbc.Diskspacev}
	GROUP BY 1
) k ON k.DatabaseName = d.DatabaseName""".format('\n     , '.join(cols), dbc=vsch.load_schema('dbc'))

		cond = []
		if names:
			pred = ' OR '.join([td.DBObjPat.search_predicate('OwnerName' if opts.owner else 'd.DatabaseName', f) for f in names])
			cond.append("({})".format(pred) if len(names) > 1 else pred)
		if opts.dbkind:
			cond.append("DBKind = '{}'".format(opts.dbkind))
		if opts.non_zero:
			cond.append("PermSpace > 0")

		if cond:
			sql += "\n WHERE " + "\n   AND ".join(cond)

		if opts.sort != 'none':
			sql += "\n ORDER BY " + {'name': 'd.DatabaseName', 'size': 'PermSpace', 'time': 'CreateTimestamp'}[opts.sort]
			if opts.reverse:
				sql += " DESC"

		return sql

def main():
	"script entry-point"
	return Database(__name__, __doc__).ls()

def args_filter(p):
	"options to filter listing"
	g = p.add_argument_group("Filters")
	g.add_argument('-o', '--owner', action='store_true', help='names to seach are owner names')
	g.add_argument("-Z", "--non-zero", action='store_true', help="only show databases with non-zero PERM space")
	x = g.add_mutually_exclusive_group()
	x.add_argument('-d', '--only-db', dest='dbkind', action='store_const', const='D', help='list only databases')
	x.add_argument('-u', '--only-users', dest='dbkind', action='store_const', const='U', help='list only users')

def args_display(p):
	"options to format the display"
	from .util import args_size
	g = p.add_argument_group("Display")
	args_size(g)

def args_order(p):
	"options to order the listing"
	from .util import args_sort
	g = p.add_argument_group("Ordering")
	args_sort(g)

if __name__ == '__main__':
	import sys
	sys.exit(main())
