#! /usr/bin/env python
"List all views that reference the given tables"

__author__ = "Paresh Adhia"
__copyright__ = "Copyright 2017, Paresh Adhia"

import tdtypes as td

logger = td.getLogger(__name__)

def main():
	"script entry-point"
	import argparse

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('tables', metavar='TBL', type=td.DBObjPat, nargs='+', help=td.DBObjPat.__doc__)
	parser.add_argument('--refs', default='SysDBA.ViewRefs', help='View References table')
	parser.add_argument('--max-depth', type=depth, default=0, help='Limit maximum depth of traversals for dependency search')
	parser.add_argument('-W', '--no-warn', dest='warn', action='store_false', help='Do not warn about stale-data')
	args = parser.parse_args()

	sql = build_sql(args.tables, refs=args.refs, depth=args.max_depth)
	with td.cursor(args) as csr:
		try:
			csr.execute(sql)
		except td.sqlcsr.Error as msg:
			if '-3807' in str(msg):
				logger.error('Error querying %s. %s', args.refs, msg)
				return 1
			raise

		if args.warn:
			logger.warning("Dependencies built from stored data, maybe stale.")
		print_trees(build_trees(csr.fetchall()))

	return 0

def depth(v):
	"assert: depth must be a +ve integer"
	if int(v) <= 0:
		raise ValueError("Must be a whole number > 0")
	return int(v)

def build_sql(tab_p, refs='SysDBA.ViewRefs', depth=0):
	"SQL query to obtain descendants of all matching objects"

	pred = '\n\t\t  OR '.join(p.search_cond() for p in tab_p)
	pred_depth = f"\n\t\tAND p.Depth <= {depth}" if depth else ""

	sql = f"""\
WITH RECURSIVE descendants AS (
	SELECT DatabaseName c_db, TableName c_name
		, c_db || '.' || c_name  VwPath
		, 1 as Depth
	FROM dbc.TablesV
	WHERE TableKind in ('T', 'O', 'V')
		AND ({pred})

	UNION ALL

	SELECT c.ViewDB, c.ViewName
		, VwPath || '>' || c.ViewDB || '.' || c.ViewName
		, Depth+1 AS Depth
	FROM {refs} c
		, descendants p
	WHERE p.c_db = c.RefDB
		AND p.c_name = c.RefName{pred_depth}
)

SELECT c_db, c_name
	, Depth
FROM descendants
ORDER BY VwPath"""

	logger.debug('SQL =>\n%s', sql)
	return sql

def build_trees(rows):
	"build hierarchical tree using the depth information"

	class View:
		"View with reference to parent and list of children"
		def __init__(self, parent, db, vw):
			self.parent, self.db, self.vw = parent, db, vw
			self.children = []

		def __str__(self):
			return self.db+'.'+self.vw

	forest = View(None, None, None)
	prev_level = 0
	parent = None

	for db, vw, level in rows:
		if level > prev_level:
			parent = parent.children[-1] if parent else forest
		else:
			while prev_level > level:
				parent = parent.parent
				prev_level -= 1

		node = View(parent, db, vw)

		if parent:
			parent.children.append(node)
		else:
			forest = node

		prev_level = level

	return forest.children

def print_trees(trees):
	"print all trees (hierarchies) that are passed in list of root nodes"
	from yappt import treeiter

	for tree in trees:
		for pfx, node in treeiter(tree):
			print(str(pfx)+str(node))

if __name__ == '__main__':
	import sys
	sys.exit(main())
