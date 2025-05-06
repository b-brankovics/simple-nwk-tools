# simple-nwk-tools
Simple python scripts for doing basic manipulations and plots of newick files

## Python3

> **If you are using a computer without a graphical user interface,** then you need to run the following `export QT_QPA_PLATFORM=offscreen`.

Installing prerequisite

```bash
conda env create -f env.yml
conda activate simple-nwk-tools
```
Create a single plot:

```bash
bin/print-single-nwk3.py -i tree.nwk -o outgroup -p tree
```

The output is an SVG file.

Create a single tree plot with metadata:

```bash
bin/print-tree.py #defaults:  -i tree.nwk -o tree.pdf
```

metadata is read from tree.yaml. (Needs to be update to be parametric)

Create plots for two trees and highlight clades that are inconflict between the
trees:

```bash
bin/print-two-nwk3.py -i tree.nwk -j tree-alt.nwk -o outgroup -p vs-test1 -q vs-test2
```