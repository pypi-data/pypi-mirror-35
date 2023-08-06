#! /usr/bin/env python
"Generate DDL for Teradata Databases from DBC tables"

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

from collections import OrderedDict
from itertools import groupby
from .util import *

_passwd = '"P@ssw0rd"'

class JrnlOpt:
	def __init__(self, opt, val):
		self.opt, self.val = opt, val

	def __str__(self):
		return '{} {} Journal'.format({'N':'No', 'S':'', 'D':'Dual', 'L':'Local'}[self.val], self.opt)

class DB:
	def __init__(self, name, *opts):
		self.name = name
		self.kind, self.owner, self.perm, self.spool, self.temp, acct, self.prot, \
			self.jrnl, self.defdb, self.date, self.role, self.prof, self.dba, self.comm = opts
		self.ownerdb = None

		self.accts = [acct]


	def ddl(self, gen_defaults=False):
		"return DDL Text"

		opts = Opts()
		opts.add('Perm', int(self.perm))
		if self.kind == 'U':
			opts.add('Password', _passwd)
		if self.ownerdb is None or self.spool != self.ownerdb.spool:
			opts.add('Spool', int(self.spool))
		if self.ownerdb is None or self.temp != self.ownerdb.temp:
			opts.add('Temporary', int(self.temp))
		if self.defdb:
			opts.add('Default Database', self.defdb)
		if self.date:
			opts.add('DateForm', {'A': 'AnsiDate', 'self': 'IntegerDate'}[self.date])
		if self.role:
			opts.add('Default Role', self.role)
		if self.prof:
			opts.add('Profile', self.prof)
		if self.ownerdb is None or self.accts[0] != self.ownerdb.accts[0]:
			opts.add('Account', quote(self.accts))
		if self.prot == 'F':
			opts.add('Fallback')
		if self.ownerdb is None or self.jrnl != self.ownerdb.jrnl:
			opts.add(JrnlOpt('Before', self.jrnl[0]))
			opts.add(JrnlOpt('After', self.jrnl[1]))
		if self.dba == 'Y':
			opts.add('DBA')

		sql = 'Create {} {} From {} As {};'.format('User' if self.kind == 'U' else 'Database', self.name, self.owner, opts)

		if self.comm:
			sql += "\nComment On {} As {};".format(self.name, quote(self.comm))

		return sql


def add_args(p):
	p.add_argument("filter", metavar='DB', nargs='+',    help="database object name")
	p.add_argument("-p", '--password',                   help="initial passord for users (default: {})".format(_passwd))
	p.add_argument(      '--full', action='store_true',  help="full DDL with default values explicitly listed")


def genddl(args):
	if args.password:
		global _passwd
		_passwd = args.password

	dblist = get_dbinfo(args.filter)

	if not args.full:
		owners = get_dbinfo([d.owner for d in dblist.values() if d.owner not in dblist])
		for db in dblist.values():
			db.ownerdb = owners.get(db.owner, dblist.get(db.owner))

	for db in dblist.values():
		yield db.ddl(args.full)


def get_dbinfo(filter):
	"Get database information"

	if not filter:
		return

	sql = """\
LOCK ROW FOR ACCESS
SELECT DatabaseName
     , RowType as DBKind
     , OwnerName
     , PermSpace
     , SpoolSpace
     , TempSpace
     , AccountName
     , ProtectionType
     , JournalFlag
     , DefaultDataBase
     , DefaultDateForm
     , RoleName
     , ProfileName
     , DBA
     , CommentString
  FROM {dbc.Dbase} T
 WHERE DatabaseName {}""".format(mk_pred(filter), dbc=dbc)

	dblist = OrderedDict([ (row[0],DB(*row)) for row in execsql(sql,'DBInfo SQL') ])

	users = [db.name for db in dblist.values() if db.kind == 'U']
	if users:
		sql = """\
SELECT A.UserName
     , A.AccountName
  FROM {dbc.AccountInfoV} A
  JOIN {dbc.Dbase} D ON D.DatabaseName = A.UserName AND D.AccountName <> A.AccountName
 WHERE UserOrProfile = 'User'
   AND UserName {}""".format(mk_pred(users),dbc=dbc)

		for db,rows in groupby(execsql(sql,'Accounts for Users SQL'), key=lambda r:r[0]):
			dblist[db].accts.extend([a for u,a in rows])

	return dblist


def main():
	import sys
	sys.exit(enter(sys.modules[__name__]))
