#! /usr/bin/env python
import csv
import scipy
import gzip
## TODO use sys.argv to catch command line arguments with i/o files

thresh=13
mincov=4
maxcov=200000

columns=["chr","pos-1","pos","ref","num.reads","read.alleles","read.quality","xchr","xpos-1","xpos","rsID","TKG.Ref","alt","af","hmm"]
data=[]
positions_dict=dict()
blacklist=[]

with gzip.open('DP2-HT51.pileup.bed.gz') as csvfile:
#with gzip.open('test.gz') as csvfile:
	for row in csv.DictReader(csvfile, fieldnames=columns, delimiter='\t'):
			row['num.reads'] = int(row['num.reads'])
			row['af'] = float(row['af'])
			## omit inconsistent data from the pileup process
			## TODO: add termination if we reject > 20% of all samples
			## current chr:pos key
			this_pos = row['chr']+":"+row['pos']
			## is this record consistent?
			if row['ref']==row['TKG.Ref']:
				data.append(row)
				## is this key already in the hash table?
				if this_pos in positions_dict: 
					this_index=len(data)-1
					## is this the third or greater duplicate
					if positions_dict[this_pos]==None:
						blacklist.append(this_index)
					else:
						initial_index = positions_dict[this_pos]
						positions_dict[this_pos]=None
						blacklist.append(initial_index)
						blacklist.append(this_index)
				## first occurence, so hash the index
				else:
					this_index=len(data)-1
					positions_dict[this_pos]=this_index

