#!bin/python3
#encoding="UTF8"

# run from  ~/DP:
# example:
# python3 filter_chromosome_names.py Sus_scrofa


import sys

chr_filename = sys.argv[1]

# get wanted chromosome names to a list (from a file)
chromosome_names = []
with open("data/chromosomes/" + chr_filename + "_with_introns_simplified_chr.txt", "r") as chr_file:
	for line in chr_file:
		line = line.strip()
		chromosome_names.append(line)
print(chromosome_names)

# now for the "*_simplified.txt" ones
# filter a file based on names from the list made above
with open("data/with_introns/" + chr_filename +  "_with_introns_simplified.txt", "r") as gff_file, \
		open("data/chromosomes/" + chr_filename + "_with_introns_simplified_chr_only.txt", "w") as only_chr_file:
	for line in gff_file:
		line = line.strip()
		chr_num = line.split()[0]
		if chr_num in chromosome_names:
			only_chr_file.write(line + "\n")
