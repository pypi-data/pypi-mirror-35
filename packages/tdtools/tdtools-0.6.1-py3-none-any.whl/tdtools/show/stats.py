#! /usr/bin/env python
"Generate DDL for Teradata Zones using DBC information"

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

from .util import *
import tdtypes as td

def add_args(p):
	p.add_argument("filter", metavar='DBObj', type=td.DBObjPat, nargs='+', help=td.DBObjPat.__doc__)

def genddl(args):
	for obj in td.DBObjPat.findall(args.filter, objtypes='TONI'):
		try:
			yield execsql('SHOW STATS ON '+str(obj), 'showstats')[0][0].replace('\r', '\n')
		except td.sqlcsr.Error as err:
			logger.error(err)

def main():
	import sys
	sys.exit(enter(sys.modules[__name__]))
