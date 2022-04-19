#!bin/python3
#encoding="UTF8"

import sys
 
def write_in_order(dictionary_of_lines, file_out):
	#seradit keys vzestupne:
	keys = [int(x) for x in dictionary_of_lines.keys()]
	sorted_keys = sorted(keys)
	# print(sorted_keys)
	for key in sorted_keys:
		key = str(key)
		file_out.write(dictionary_of_lines[key] + "\n")

species_name = sys.argv[1]
LoadingExons = False

with open("data/ready_to_use/without_N/" + species_name + "_no_duplicates_without_N.txt", "r") as file_in,\
	open("data/ready_to_use/without_N/sorted_introns_exons/" + species_name + "_no_duplicates_without_N_sorted.txt", "w") as file_out:

	IntronExonGroup = {}
	# nacist radky intron, exon
	# az najdu exon, zapsat vse na stridacku
	# nezapomenout zapsat posledni radky
	for line in file_in:
		line = line.strip()
		line_list = line.split()

		IntronExon = line_list[1]
		IntronExonStart = line_list[2]

		if IntronExon == "exon":
			if IntronExonGroup == {}:
				LoadingExons = True
			if LoadingExons == True:
				IntronExonGroup[IntronExonStart] = line
			else: # narazi na exon po intronech
				write_in_order(IntronExonGroup, file_out)
				IntronExonGroup = {}
				IntronExonGroup[IntronExonStart] = line
				# print(IntronExonGroup)
				LoadingExons = True			
		else: # intron
			LoadingExons = False
			IntronExonGroup[IntronExonStart] = line

	#last section
	write_in_order(IntronExonGroup, file_out)