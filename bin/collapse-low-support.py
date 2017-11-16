#!/usr/bin/python
from ete2 import Tree

import sys, getopt

def main(argv):
	inputfile = ''
	outgroup = ''
	minimal = 0
	try:
		opts, args = getopt.getopt(argv,"hi:m:o:",["input=","min=","outgroup="])
	except getopt.GetoptError:
		print 'collapse-low-support -i <inputfile> -o <outgroup> -m <min support>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'collapse-low-support -i <inputfile> -o <outgroup> -m <min support>'
			sys.exit()
		elif opt in ("-i", "--input"):
			inputfile = arg
		elif opt in ("-o", "--outgroup"):
			outgroup = arg
		elif opt in ("-m", "--min"):
			minimal = float(arg)
	# read tree
	t = Tree(inputfile)
	t.set_outgroup(outgroup)

	for node in t.traverse("preorder"):
		if not node.is_leaf():
			if not node.is_root():
				if (float(node.support) < minimal):
					#print float(node.support), node.name
					for child in node.children:
						child.dist = child.dist + node.dist
					node.delete()


	# ladderize
	t.ladderize(1)
	# print final tree
	print t.write()

#	print outgroup, minimal

if __name__ == "__main__":
	main(sys.argv[1:])

