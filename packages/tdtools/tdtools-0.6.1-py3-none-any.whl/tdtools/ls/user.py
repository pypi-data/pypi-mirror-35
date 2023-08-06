#! /usr/bin/env python

"List Teradata Users"

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
from .util import args_size

class User(Listing):
	"User listing"

	def user_args(self):
		yield lambda p: p.add_argument("names", metavar='USER', nargs='*', help="search for only specific names (wild-cards allowed)")
		yield lambda p: p.add_argument("-p", "--profile", action="store_true", help="names to search are profile names (default usernames)")
		yield args_size

	def all_cols(self, opts):
		# pylint: disable=locally-disabled, bad-whitespace
		return [
			  Col("D.DatabaseName",                          "User",    0)

			, Col("D.ProfileName",                           "Prof",    1)
			, Col("COALESCE(P.DefaultDB,D.DefaultDatabase)", "DB",      1)
			, Col("D.PermSpace",                             "Perm_",   1)
			, Col("COALESCE(P.SpoolSpace,D.SpoolSpace)",     "Spool_",  1)
			, Col("COALESCE(P.TempSpace,D.TempSpace)",       "Temp_",   1)

			, Col("COALESCE(P.DefaultAccount,AccountName)",  "Acct",    2)
			, Col("CAST(D.LockedDate As Date)",              "Locked",  2)
			, Col("CAST(CAST(CAST(D.LockedTime As FORMAT '99:99:99') AS CHAR(8)) AS TIME(0))",  "LTime", 3)
			, Col("CAST(D.CreateTimeStamp AS DATE)",         "Created", 2)
			, Col("CAST(D.CreateTimeStamp AS TIME)",         "CTime",   3)
			, Col("D.CommentString",                         "Note",    2)

			, Col("D.OwnerName",                             "Owner",   3)
			, Col("D.CreatorName",                           "Creator", 3)
			, Col("D.LastAlterTimeStamp",                    "Altered", 3)
		]

	def build_sql(self, names, cols, opts):
		from .. import vsch

		if names:
			pred = ' OR '.join([td.DBObjPat.search_predicate('D.ProfileName' if opts.profile else 'DatabaseName', f) for f in names])
			pred = "\n   AND {}".format(pred if len(names) == 1 else '('+pred+')')
		else:
			pred = ''

		return """\
SELECT {}
  FROM {dbc.dbase} D
  LEFT JOIN {dbc.ProfileInfoV} P ON P.ProfileName = D.ProfileName
 WHERE RowType = 'U'{}
 ORDER BY 1""".format('\n     , '.join(cols), pred, dbc=vsch.load_schema('dbc'))


def main():
	"script entry-point"
	return User(__name__, __doc__).ls()


if __name__ == '__main__':
	import sys
	sys.exit(main())
