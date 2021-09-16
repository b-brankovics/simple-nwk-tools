#!/usr/bin/python3
import PyQt5
from ete3 import Tree, TreeStyle, NodeStyle

import sys, getopt

def main(argv):
	inputfile = ''
	outgroup = ''
	outputfile = ''

	ts = TreeStyle()
	ts.show_leaf_name = True
	ts.show_branch_length = False
	ts.show_branch_support = True

	ns = NodeStyle()
	ns["size"] = 0
	ns["vt_line_width"] = 2
	ns["hz_line_width"] = 2

	try:
		opts, args = getopt.getopt(argv,"hi:o:p:",["input=","outgroup=","-prefix-svg="])
	except getopt.GetoptError:
		print('print-single-nwk.py -i <inputfile> -o <outgroup> -p <prefixsvg>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('print-single-nwk.py -i <inputfile> -o <outgroup> -p <prefixsvg>')
			sys.exit()
		elif opt in ("-i", "--input"):
			inputfile = arg
		elif opt in ("-o", "--outgroup"):
			outgroup = arg
		elif opt in ("-p", "--prefix-svg"):
			outputfile = arg
	# read tree
	t = Tree(inputfile)
	t.set_outgroup(outgroup)
	t.ladderize(1)

	for node in t.traverse():
		node.set_style(ns)

	# print final tree
	t.render(outputfile + ".svg", tree_style=ts)

#	print outgroup, minimal

if __name__ == "__main__":
	main(sys.argv[1:])

