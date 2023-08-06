#! /usr/bin/env python
"Wrapper around Teradata's SHOW command"

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

import sys
import os
import os.path as p

from itertools import groupby
from tdtypes.sqlcsr import Error
from .util import *

obj_t = {'T':'Table', 'O':'Table', 'V':'View', 'C':'Temporary Table', 'I':'Join Index', 'G':'Trigger',
	'M':'Macro', 'F':'Specific Function', 'S':'Function', 'R':'Function', 'P':'Procedure', 'E':'Procedure'}

class DBObj:
	"Teradata object of a kind"
	def __init__(self, sch, name, kind):
		self.sch, self.name, self.kind = sch, name, kind

	def __str__(self):
		return '"{}"."{}"'.format(self.sch, self.name)

def add_args(argp):
	"Add arguments to the passed parser"
	from datetime import datetime

	ArgDate = lambda d: datetime.strptime(d, '%Y-%m-%d')

	# pylint: disable=locally-disabled, bad-whitespace, multiple-statements
	argp.add_argument("filter",           metavar='DBObj', nargs='+',   help="database object name")
	argp.add_argument("-t", '--type',     metavar='KIND',  choices = obj_t, dest="types", action='append', help="limit objects to selected types ({})".format(','.join(sorted(obj_t))))
	argp.add_argument(      '--show-db',  action='store_true',          help="set default database before object definition")
	argp.add_argument(      '--no-stats', dest='stats',    default=True, action='store_false', help="do not generate stats defintions for table and JI")
	argp.add_argument(      '--since',    metavar='YYYY-MM-DD', type=ArgDate, help="only consider objects ALTERed since the given date")
	argp.add_argument(      '--before',   metavar='YYYY-MM-DD', type=ArgDate, help="only consider objects ALTERed before the given date")
	argp.add_argument('-w', '--write',    action='store_true',          help='create a file for each database object')


def genddl(args):
	"DDL generator"
	for typ, grp1 in groupby(getobjs(args.filter, args.types, args.since, args.before), key=lambda o: o.kind):
		for db, grp2 in groupby(grp1, key=lambda o: o.sch):
			if args.show_db:
				yield '\nDatabase {0};\n'.format(db)
			for o in grp2:
				try:
					yield obj_ddl(o, args.write, args.stats)
				except Error as msg:
					logger.warning("Skipped {}, error:{}'".format(o, msg))

def getobjs(objects, types, since=None, before=None):
	"return object lists based on passed criteria"

	def mk_pred(dbtb):
		"make SQL boolean predicate to search for database and tablename"
		db, tb = dbtb.split('.') if '.' in dbtb else (dbtb, None)
		dbq = "T.DatabaseName {} '{}'".format('like' if '%' in db else '=', db)
		if tb == None:
			return dbq
		return "({} and T.TableName {} '{}')".format(dbq, 'like' if '%' in tb else '=', tb)

	sql = """\
SELECT T.DatabaseName,
    COALESCE(F.SpecificName, T.TableName),
    T.TableKind
FROM {dbc.TablesV} T
LEFT JOIN {dbc.FunctionsV} F ON F.DatabaseName = T.DatabaseName AND F.FunctionName = T.TableName
WHERE ({})""".format( '\n    OR  '.join([mk_pred(dbtb) for dbtb in objects]), dbc=dbc )

	if types:
		sql += "\n   AND TableKind IN {0}".format(quote(types))
	if since:
		sql += "\n   AND LastAlterTimestamp >= CAST('{}' AS TIMESTAMP(0))".format(since.isoformat())
	if before:
		sql += "\n   AND LastAlterTimestamp <  CAST('{}' AS TIMESTAMP(0))".format(before.isoformat())

	sql += """
ORDER BY
	CASE TableKind
		WHEN 'T' THEN 0
		WHEN 'O' THEN 0
		WHEN 'C' THEN 0
		WHEN 'G' THEN 1
		WHEN 'I' THEN 2
		WHEN 'V' THEN 3
		ELSE 4
	END,
	CreateTimestamp"""

	return [DBObj(db, ob, k) for db, ob, k in execsql(sql, 'Object list SQL')]

def obj_ddl(obj, write, stats):
	"Object DDL generator"
	def show(sql):
		"return cleansed DDL"
		return ''.join([l[0].replace('\r', '\n') for l in execsql('SHOW ' + sql)]).rstrip().rstrip(';') + ';'

	if obj.kind in obj_t:
		ddl = show('{} "{}"."{}"'.format(obj_t[obj.kind], obj.sch, obj.name))
	else:
		logger.error('SHOW command is not supported for {}'.format(obj))
		return ''

	if stats and obj.kind in ['T', 'O', 'N', 'I']:
		try:
			ddl += '\n\n' + show('STATS ON "{}"."{}"'.format(obj.sch, obj.name))
		except Error:
			logger.info('SHOW STATS ON {} failed.'.format(str(obj)))

	if write:
		mk_dbfolder(obj.sch)
		fname = p.join(obj.sch, obj.name + '.' + {'P':'sp'}.get(obj.kind, 'sql'))
		logger.debug('Writing DDL of "{}" to "{}"'.format(obj, fname))
		with open(fname, 'w') as out:
			print(ddl, file=out)
		return '.{} file={}'.format('compile' if obj.kind == 'P' else 'run', fname)

	else:
		return ddl + '\n'

folders = set()
def mk_dbfolder(db):
	"Create a folder with same name as DATABASE"
	if db in folders:
		return

	if not p.exists(db):
		os.mkdir(db)
	elif not p.isdir(db):
		raise Err('[{}] exists and is not a directory'.foramt(db))

	folders.add(db)

def main():
	"script entry-point"
	sys.exit(enter(sys.modules[__name__]))
