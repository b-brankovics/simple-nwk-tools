# simple-nwk-tools
Simple python scripts for doing basic manipulations and plots of newick files

## Python3

> **If you are using a computer without a graphical user interface,** then you need to run the following `export QT_QPA_PLATFORM=offscreen`.

Installing prerequisite
```
pip3 install pyqt5
pip3 install ete3
pip3 install numpy
```

Create a single plot:
```
python3 bin/print-single-nwk3.py -i tree.nwk -o outgroup -p tree
```

The output is an SVG file.

Create a single tree plot with metadata:
```
bin/print-tree.py #defaults:  -i tree.nwk -o tree.pdf
```

metadata is read from tree.yaml. (Needs to be update to be parametric)
