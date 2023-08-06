#! /usr/bin/env python

"Show statistics on Teradata objects"

import xml.etree.ElementTree as ET

from tdtypes.sqlcsr import Error
import tdtypes as td
from tdtools import util

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2016-2017, Paresh Adhia"

logger = util.getLogger(__name__)

def main():
	"script entry point"
	from argparse import ArgumentParser

	p = ArgumentParser(description=__doc__)

	p.add_argument("tblist", type=td.DBObjPat, nargs='+', help=td.DBObjPat.__doc__)
	td.dbconn_args(p)

	args = p.parse_args()

	with td.cursor(args) as csr:
		def tbl_stats(tbl):
			"Table stats in a tablular form"
			try:
				import yappt

				csr.execute('SHOW IN XML STATS VALUES ON ' + str(tbl))
				stats = [xml2stats(s) for s in ET.fromstring(csr.fetchxml()).findall('./Statistics')]
				return str(tbl) + '\n' + yappt.tabulate(stats, columns=['Column', 'Time', ('Card', yappt.HumanInt), 'Nulls', 'Samp', 'Chg%', 'Age'])
			except Error:
				logger.warning('Unable to obtain statistics information for {}'.format(tbl))

		print('\n\n'.join(st for st in (tbl_stats(tbl) for tbl in td.DBObjPat.findall(args.tblist, objtypes='TONI')) if st))


def xml2stats(s):
	"parse XML and return a list of stats tuples"

	rows = nulls = collts = samp = thr_age = thr_chg = None
	if s.find('./StatsDefinition/StatsEntries/StatsEntry/Alias') is not None:
		col = [s.find('./StatsDefinition/StatsEntries/StatsEntry/Alias').text]
	else:
		col = [c.text.rstrip() for c in s.findall('./StatsDefinition/StatsEntries/StatsEntry/Expr')]

	stat = s.find('./Histogram/SummaryInfo/NumOfDistinctVals')
	if stat != None:
		rows = int(stat.text)

	stat = s.find('./TableLevelSummary/SummaryRecord/RowCount')
	if stat != None:
		rows = int(stat.text)

	stat = s.find('./TableLevelSummary/SummaryRecord/TimeStamp')
	if stat != None:
		collts = stat.text[:10]
	else:
		stat = s.find('./Histogram/SummaryInfo/TimeStamp')
		if stat != None:
			collts = stat.text[:10]

	stat = s.find('./Histogram/SummaryInfo/NumOfNulls')
	if stat is not None:
		nulls = int(stat.text)

	stat = s.find('./StatsDefinition/Using')
	if stat != None:
		for x in stat:

			val = x.attrib.get('value')
			if val:
				val = float(val)

			if x.tag == 'Threshold':
				if x.attrib['typecode'] == 'C': thr_chg = val
				elif x.attrib['typecode'] == 'T': thr_age = val
			elif x.tag == 'Sample':
				samp = val

	return (','.join(col) or '*', collts, rows, nulls, samp, thr_chg, thr_age)


if __name__ == '__main__':
	import sys
	sys.exit(main())
