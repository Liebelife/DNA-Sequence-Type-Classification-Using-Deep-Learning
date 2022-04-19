#!bin/python3
#encoding="UTF8"

# running the code example:
# from ~/DP/
# python3 filter_fasta.py Sus_scrofa

# saves results to ~/DP/data/ready_to_use


import sys

species_name = sys.argv[1]

# load chromosome numbers (only)
# example file Sus_scrofa_with_introns_simplified_chr.txt
chr_list = []
with open("data/chromosomes/" + species_name + "_with_introns_simplified_chr.txt", "r") as file:
		for line in file:
			line = line.strip()
			chr_list.append(line)

# load chromosome sequences to a dictionary
chromosome_list = {}
with open("data/" + species_name + ".fna", "r") as fasta:
	sequence = ""
	chr_name_saved = ""
	write_sequence = False
	for line in fasta:
		line = line.strip()
		if line.startswith(">"):
			chr_name = line.split()[0].strip(">")
			if chr_name_saved == "": 
				if chr_name in chr_list:
					write_sequence = True
					chr_name_saved = chr_name
					sequence = ""
			# case: saving a new name:sequence pair to dictionary
			else:
				chromosome_list[chr_name_saved] = sequence
				if chr_name in chr_list:
					chr_name_saved = chr_name
					write_sequence = True
					sequence = ""
				else:
					write_sequence = False
					chr_name_saved = ""
		else:
			if write_sequence == True:
				sequence += line
# for k,v in chromosome_list.items():
# 	print(k,v[-100:])


# NC_010462.3     exon    148946  149214
# NC_010462.3     exon    150486  150574
all_exons = 0
all_introns = 0
problematic_exons = 0
problematic_introns = 0
with open("data/chromosomes/" + species_name + "_with_introns_simplified_chr_only_no_duplicates.txt", "r") as extracted_gff,\
	open("data/ready_to_use/" + species_name + "_no_duplicates.txt", "w") as file_out,\
	open("data/ready_to_use/" + species_name + "_error_info_no_duplicates.txt", "w") as file_error:
	for line in extracted_gff:
		line = line.strip()

		line_split = line.split()
		chr_number = line_split[0]
		identifier = line_split[1]
		start = int(line_split[2])
		stop = int(line_split[3])

		# start - 1 kvuli indexaci od 1
		sequence = chromosome_list[chr_number][start-1:stop]
		if identifier == "exon":
			all_exons += 1
			if "N" in sequence:
				problematic_exons += 1
				file_error.write("POZOR, máme 'N' v sekvenci:\n" + line + sequence + "\n")
		else:
			all_introns += 1
			if "N" in sequence:
				problematic_introns += 1
		file_out.write(line + "\t" + sequence + "\n")

	exon_report = f"pocet exonu obsahujicich N: {problematic_exons} ({(problematic_exons/all_exons) * 100} %)"
	print(exon_report)
	file_error.write(exon_report+"\n")

	intron_report = f"pocet intronu obsahujicich N: {problematic_introns} ({(problematic_introns/all_introns) * 100} %)"
	print(intron_report)
	file_error.write(intron_report+"\n")