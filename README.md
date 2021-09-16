# simple-nwk-tools
Simple python scripts for doing basic manipulations and plots of newick files

## Python3

> **You need to use computer with a graphical user interface!**

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