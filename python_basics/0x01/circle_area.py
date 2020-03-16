#!/usr/bin/python
import sys
if len(sys.argv) != 2:
    print "Error: Usage is", sys.argv[0], "radius"
else:
    area = 3.14 * (float(sys.argv[1]) ** 2)
    print "Area:", area
