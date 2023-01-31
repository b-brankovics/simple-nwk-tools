#!/usr/bin/env python3

#import PyQt5
from ete3 import Tree, faces, TreeStyle, NodeStyle

import os.path, sys, getopt

def main(argv):
	inputfile = 'tree.nwk'
#	outgroup = ''
	metadatafile = 'tree.yaml'
	outputfile = 'tree.pdf'

	ts = TreeStyle()
	ts.show_leaf_name = True
	ts.show_branch_length = False
	ts.show_branch_support = True

	ns = NodeStyle()
	ns["size"] = 0
	#ns["vt_line_width"] = 2
	#ns["hz_line_width"] = 2

	try:
		opts, args = getopt.getopt(argv,"hi:o:m:",["input=","-output=","-metadata="])
                #opts, args = getopt.getopt(argv,"hi:o:p:",["input=","outgroup=","-prefix-svg="])
	except getopt.GetoptError:
		print('print-single-nwk.py -i <inputfile> -o <output> -m <metadata.yaml>')
                #print('print-single-nwk.py -i <inputfile> -o <outgroup> -p <prefixsvg>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('print-single-nwk.py -i <inputfile> -o <output> -m <metadata.yaml>')
                        # print('print-single-nwk.py -i <inputfile> -o <outgroup> -p <prefixsvg>')
			sys.exit()
		elif opt in ("-i", "--input"):
			inputfile = arg
		#elif opt in ("-o", "--outgroup"):
		#	outgroup = arg
		elif opt in ("-o", "--output"):
			outputfile = arg
		elif opt in ("-m", "--metadata"):
			metadatafile = arg
	# read tree
	t = Tree(inputfile)
	#t.set_outgroup(outgroup)
#	t.ladderize(1)

	for node in t.traverse():
		node.set_style(ns)

	# Read metadata and add to tree
	if os.path.isfile(metadatafile):
		import yaml
		from yaml.loader import SafeLoader
		with open(metadatafile, 'r') as f:
			info = list(yaml.load_all(f, Loader=SafeLoader))
	
		id2meta = info[0]
		# Add metadata to the tree
		def mylayout(node):
			if node.is_leaf():
				textvalue = ''
				if node.name in id2meta:
					textvalue = id2meta[node.name]
			
				descFace = faces.TextFace(textvalue, fstyle="italic")
        		# position: “branch-right”, “branch-top”, “branch-bottom”, “float”, “float-behind” and “aligned”
				faces.add_face_to_node(descFace, node, column=1, position="aligned")#, aligned=True)
    
		ts.layout_fn = mylayout
	else:
		print(f"Warning: metadatafile ('{metadatafile}') does not exist, skipping metadata step")

	# print final tree
	t.render(outputfile, tree_style=ts)


if __name__ == "__main__":
	main(sys.argv[1:])

