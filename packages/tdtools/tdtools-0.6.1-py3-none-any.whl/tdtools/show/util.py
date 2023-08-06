"Common functions used by show*.py utilities"

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

from tdtypes import sqlcsr
from .. import vsch
from .. import util

logger = util.getLogger(__name__)

dbc = vsch.load_schema('dbc')

class Err(Exception): pass

class Opts(list):
	def __init__(self, init=None):
		super().__init__()
		if init:
			for o, v in init:
				self.add(o, v)

	def add(self, opt, val=''):
		if val != None:
			self.append((opt, val))

	@staticmethod
	def _opt2str(opt,val):
		if type(val) == int:
			if   val       == 0: pass
			elif val % 1e9 == 0: val = '{}e9'.format(int(val//1e9))
			elif val % 1e6 == 0: val = '{}e6'.format(int(val//1e6))
			elif val % 1e3 == 0: val = '{}e3'.format(int(val//1e3))
		elif type(val) == list:
			val = '({})'.format(','.join(str(val))) if len(val) > 1 else str(val[0])

		return '{}={}'.format(opt, val) if str(val) != '' else str(opt)

	def __str__(self):
		return ', '.join([Opts._opt2str(o, v) for o, v in self])


def quote(ident):
	if ident is None:
		return None

	if isinstance(ident, list):
		return "(" + ', '.join([quote(i) for i in ident]) + ")"

	return "'{}'".format(ident.replace("'", "''"))


def execsql(sql, msg='SQL'):
	logger.debug(msg + ':\n' + sql)
	sqlcsr.csr.execute(sql)

	return list(sqlcsr.csr.fetchall())


def mk_pred(names):
	op = 'Like ' if [o for o in names if '%' in o] else '= '
	if len(names) > 1:
		return op + 'Any ' + quote(names)
	else:
		return op + quote(names[0])


def enter(mod):
	rc = 8

	try:
		from argparse import ArgumentParser

		p = ArgumentParser(description=mod.__doc__)

		mod.add_args(p)
		sqlcsr.dbconn_args(p)

		args = p.parse_args()

		with sqlcsr.cursor(args) as csr:
			for ddl in mod.genddl(args):
				print(ddl)

		rc = 0

	except Err as msg:
		logger.error(msg)
	except Exception as msg:
		logger.exception(msg)

	return rc
