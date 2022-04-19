import sys

# run from cmd ~/DP/ and save report to file *.txt:
# ./filter_fasta_for_all.sh python3 filter_N_free_fasta.py > N_free_report.txt

species_name = sys.argv[1]

deleted_lines = 0
all_lines = 0
with open("data/ready_to_use/" + species_name + "_no_duplicates.txt", "r") as file_in,\
	open("data/ready_to_use/without_N/" + species_name + "_no_duplicates_without_N.txt", "w") as file_out:
		for line in file_in:
			line = line.strip()
			line_list = line.split()
			all_lines += 1

			if len(line_list) < 5: # intron dlouhy 1? proste chybi sekvence
				deleted_lines += 1
			else:
				sequence = line_list[4]
				if "N" not in sequence:
					file_out.write(line + "\n")
				else:
					deleted_lines += 1
print(f"smazano {deleted_lines} sekvenci, celkem {deleted_lines/all_lines * 100} %")