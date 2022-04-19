#!bin/python3
#encoding="UTF8"

import sys

species_name = sys.argv[1]

with open("data/chromosomes/" + species_name + "_with_introns_simplified_chr_only.txt", "r") as file_in,\
	open("data/chromosomes/" + species_name + "_with_introns_simplified_chr_only_no_duplicates.txt", "w") as file_out:
	lines_seen = set() # holds lines already seen
	for line in file_in:
	    if line not in lines_seen: # not a duplicate
	        file_out.write(line)
	        lines_seen.add(line)