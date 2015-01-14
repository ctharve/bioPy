r! /usr/bin/env python
## filter  reads lacking sufficient
## differences in mappability to multiple positions in the genome
import sys

# TODO: ensure line by line processing
#line = sys.stdin.readlines()
thresh = 10

for ii in sys.stdin: 
	
	if ii[0] == "@":
		print ii.strip()	
	else:
		aStart = ii.find("AS:i:")
		asNum = (ii[aStart+5:aStart+7]).strip()
		
		xStart = ii.find("XS:i")
		xsNum = (ii[xStart+5:xStart+7]).strip()

		if abs(int(asNum)-int(xsNum)) >= thresh:
			print ii.strip()
