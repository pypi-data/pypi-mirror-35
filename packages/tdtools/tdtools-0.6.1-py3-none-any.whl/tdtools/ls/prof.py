#! /usr/bin/env python
"List Teradata profiles"

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

class Profile(Listing):
	"Profile Listing"

	def user_args(self):
		yield lambda p: p.add_argument("names", metavar='PROFILE', nargs='*', help="search for only specific names (wild-cards allowed)")
		yield args_size

	def all_cols(self, opts):
		# pylint: disable=locally-disabled, bad-whitespace
		return [
			  Col("ProfileName",    "Prof",   0)

			, Col("SpoolSpace",     "Spool_", 1)
			, Col("TempSpace",      "Temp_",  1)
			, Col("DefaultDB",      "DB",     1)
			, Col("DefaultAccount", "Acct",   1)

			, Col("QueryBand",      "QB",     2)
			, Col("CommentString",  "Note",   2)
		]

	def build_sql(self, names, cols, opts):
		from .. import vsch

		if names:
			where = "\n WHERE " + ' OR '.join([td.DBObjPat.search_predicate('ProfileName', f) for f in names])
		else:
			where = ''

		return """\
SELECT {}
  FROM {dbc.ProfileInfoV}{}
 ORDER BY 1""".format('\n     , '.join(cols), where, dbc=vsch.load_schema('dbc'))


def main():
	"script entry-point"
	return Profile(__name__, __doc__).ls()

if __name__ == '__main__':
	import sys
	sys.exit(main())
