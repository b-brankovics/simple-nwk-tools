#!/usr/bin/python
from ete2 import Tree, TreeStyle, NodeStyle

import sys, getopt

def main(argv):
	inputfile1 = ''
	inputfile2 = ''
	outgroup = ''
	outputfile1 = ''
	outputfile2 = ''

	ts = TreeStyle()
	ts.show_leaf_name = True
	ts.show_branch_length = False
	ts.show_branch_support = True

	ns1 = NodeStyle()
	ns1["size"] = 0
	ns1["vt_line_width"] = 2
	ns1["hz_line_width"] = 2
	ns1["vt_line_type"] = 2 # 0 solid, 1 dashed, 2 dotted
	ns1["hz_line_type"] = 2 # 0 solid, 1 dashed, 2 dotted
	ns1["vt_line_color"] = "#FF0000"
	ns1["hz_line_color"] = "#FF0000"

	ns2 = NodeStyle()
	ns2["size"] = 0
	ns2["vt_line_width"] = 2
	ns2["hz_line_width"] = 2
	ns2["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
	ns2["hz_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted


	try:
		opts, args = getopt.getopt(argv,"hi:j:o:p:q:",["input1=","input2=","outgroup=","-prefix-svg1=","-prefix-svg2="])
	except getopt.GetoptError:
		print 'print-two-nwk.py -i <inputfile1> -j <inputfile2> -o <outgroup> -p <prefixsvg1> -q <prefixsvg2>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'print-two-nwk.py -i <inputfile1> -j <inputfile2> -o <outgroup> -p <prefixsvg1> -q <prefixsvg2>'
			sys.exit()
		elif opt in ("-i", "--input1"):
			inputfile1 = arg
		elif opt in ("-j", "--input2"):
			inputfile2 = arg
		elif opt in ("-o", "--outgroup"):
			outgroup = arg
		elif opt in ("-p", "--prefix-svg1"):
			outputfile1 = arg
		elif opt in ("-q", "--prefix-svg2"):
			outputfile2 = arg
	# read tree
	t1 = Tree(inputfile1)
	t1.set_outgroup(outgroup)
	t1.ladderize(1)

	t2 = Tree(inputfile2)
	t2.set_outgroup(outgroup)
	t2.ladderize(1)

	# check clades
	clades = dict()

	for node in t1.traverse():
		if not node.is_leaf():
			# Get leaf names for a "node"
			names = map(lambda n: n.name, node.iter_leaves())
			names.sort()
			cladename = ",".join(names)
			if cladename in clades:
				clades[cladename] += 1
			else:
				clades[cladename] = 1

	for node in t2.traverse():
		if not node.is_leaf():
			# Get leaf names for a "node"
			names = map(lambda n: n.name, node.iter_leaves())
			names.sort()
			cladename = ",".join(names)
			if cladename in clades:
				clades[cladename] += 1
			else:
				clades[cladename] = 1


	for node in t1.traverse():
		if not node.is_leaf():
			# Get leaf names for a "node"
			names = map(lambda n: n.name, node.iter_leaves())
			names.sort()
			cladename = ",".join(names)
			if clades[cladename] == 2:
				node.set_style(ns2)
			else:
				node.set_style(ns1)
		else:
			node.set_style(ns2)

	for node in t2.traverse():
		if not node.is_leaf():
			# Get leaf names for a "node"
			names = map(lambda n: n.name, node.iter_leaves())
			names.sort()
			cladename = ",".join(names)
			if clades[cladename] == 2:
				node.set_style(ns2)
			else:
				node.set_style(ns1)
		else:
			node.set_style(ns2)

	# print final tree
	t1.render(outputfile1 + ".svg", tree_style=ts)
	t2.render(outputfile2 + ".svg", tree_style=ts)

#	print outgroup, minimal

if __name__ == "__main__":
	main(sys.argv[1:])

