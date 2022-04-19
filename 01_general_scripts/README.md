09/2021
Eliška Lieberzeitová - diplomová práce

to start the rsub, activate conda bio env first
agat is in agat environment

Mus_musculus                
Monodelphis_domestica       
Sus_scrofa                  
Felis_catus                 
Bos_taurus                  
Equus_caballus 
Canis_lupus_familiaris     
Rattus_norvegicus  
Ovis_aries      
Ornitohoryhynchus_anatinus

genome sequence, genome GFF annotation:

Mus musculus	https://www.ncbi.nlm.nih.gov/genome/52?genome_assembly_id=992563
Felis catus	https://www.ncbi.nlm.nih.gov/genome/78?genome_assembly_id=356698
Rattus norvegicus	https://www.ncbi.nlm.nih.gov/genome/73?genome_assembly_id=1535500
Bos taurus	https://www.ncbi.nlm.nih.gov/genome/82?genome_assembly_id=371813
Sus scrofa	https://www.ncbi.nlm.nih.gov/genome/84?genome_assembly_id=317145
Ovis aries	https://www.ncbi.nlm.nih.gov/genome/83?genome_assembly_id=1549124
Canis lupus familiaris	https://www.ncbi.nlm.nih.gov/genome/85?genome_assembly_id=984575
Equus caballus	https://www.ncbi.nlm.nih.gov/genome/145?genome_assembly_id=358900
Ornitohoryhynchus anatinus	https://www.ncbi.nlm.nih.gov/genome/110?genome_assembly_id=1567774
Monodelphis domestica	https://www.ncbi.nlm.nih.gov/genome/220?genome_assembly_id=28569

#### script overview (in order needed for obtaining data):
*download_data.sh* - to download genomes in .fna form and their .gff (the ones listed above) do a folder data (run script from the DP folder) 

*rename_files.sh* - rename gff and fna files in the data folder and unzip them

*add_introns.sh* - adds introns to .fna files in /data/ to /data/with_introns/\*.gff using the AGAT tool ('conda activate agat' needed)

*get_intron_exon_coordinates.sh* - used in the get_coordinates_for_all_gff.sh script
*get_coordinates_for_all_gff.sh* - to create data/with_introns/*_simplified.txt file containing chromosome number, start and stop sequence for introns and exons

*select_chromosomes.sh*  - get chromosome names from .fna (tvori data/chromosomes/\*_chr.txt)

now remove the MT chromosomes by hand

*filter_chromosome_names.py* - filters the lines chr, start, stop into a new file where only selected chromosomes are present (creates data/chromosomes/\*_with_introns_simplified_chr_only.txt) - use the script for looping over all files (./filter_fasta_for_all.sh filter_chromosome_names.py )

*remove_duplicated_lines.py* - removes duplicate lines in the chromosome number, start and stop .txt file (from data/chromosomes/\*_with_introns_simplified_chr_only.txt saves to data/chromosomes/\*with_introns_simplified_chr_only_no_duplicates.txt)             
*remove_duplicated_lines_for_all.sh* - uses remove_duplicated_lines.py script for all

*filter_fasta.py*  - saves results to ~/DP/data/ready_to_use. adds the fasta sequence of introns and exons to the .txt file data/ready_to_use/\*_no_duplicates.txt"
*filter_fasta_for_all.sh*  - use: ./filter_fasta_for_all.sh filter_fasta.py
      
*filter_N_free_fasta.py* - filters out exons and introns containing "N" and creates a report of how many sequences (absolute numbers and also % were removed). To run for all use *filter_fasta_for_all.sh* with the sript name as an argument)
*filter_fasta_report.txt*  - contains info about previous script run

*order_introns_exons.py* - NOT NEEDED (solved with the following one-liner .sh script order_introns_exons_for_all.sh :)))

*order_introns_exons_for_all.sh* - sorts exons and exons according to their start coordinate and chromosome number (data preparation for transformer)

wget (fna + gff)
gunzip both
grep "exon" GCF_000181335.3_Felis_catus_9.0_genomic.gff | cut -f 4,5
head data/*.txt
find | grep Felis
find ./data/ -name *Felis*

former names:
Mus_musculus				GCF_000001635.27_GRCm39_genomic
Monodelphis_domestica		GCF_000002295.2_MonDom5_genomic
Sus_scrofa					GCF_000003025.6_Sscrofa11.1_genomic
Felis_catus					GCF_000181335.3_Felis_catus_9.0_genomic
Bos_taurus					GCF_002263795.1_ARS-UCD1.2_genomic
Equus_caballus				GCF_002863925.1_EquCab3.0_genomic
Canis_lupus_familiaris		GCF_014441545.1_ROS_Cfam_1.0_genomic
Rattus_norvegicus			GCF_015227675.2_mRatBN7.2_genomic
Ovis_aries					GCF_016772045.1_ARS-UI_Ramb_v2.0_genomic
Ornitohoryhynchus_anatinus	GCF_004115215.2_mOrnAna1.pri.v4_genomic

renaming files - used command example:
rename former_prefix new_prefix files_to_be_affected
rename GCF_000001635.27_GRCm39_genomic Mus_musculus GCF_000001635.27_GRCm39_genomic*
rename GCF_000003025.6_Sscrofa11.1_genomic Sus_scrofa GCF_000003025.6_Sscrofa11.1_genomic*
rename GCF_000181335.3_Felis_catus_9.0_genomic Felis_catus GCF_000181335.3_Felis_catus_9.0_genomic*
rename GCF_002263795.1_ARS-UCD1.2_genomic Bos_taurus	 GCF_002263795.1_ARS-UCD1.2_genomic*
rename GCF_002863925.1_EquCab3.0_genomic Equus_caballus GCF_002863925.1_EquCab3.0_genomic*
rename GCF_014441545.1_ROS_Cfam_1.0_genomic Canis_lupus_familiaris GCF_014441545.1_ROS_Cfam_1.0_genomic*
rename GCF_015227675.2_mRatBN7.2_genomic Rattus_norvegicus GCF_015227675.2_mRatBN7.2_genomic*
rename GCF_016772045.1_ARS-UI_Ramb_v2.0_genomic Ovis_aries	 GCF_016772045.1_ARS-UI_Ramb_v2.0_genomic*
rename GCF_004115215.2_mOrnAna1.pri.v4_genomic Ornitohoryhynchus_anatinus GCF_004115215.2_mOrnAna1.pri.v4_genomic.*

in .gff file there is a list of chromosomes (starting with NC_), MT DNA (NC_006853.1) and unmatched scaffolds (starting with NW_)
example for Bos Taurus:
NC_006853.1
NC_037328.1
NC_037329.1
NC_037330.1
NC_037331.1
NC_037332.1
NC_037333.1
NC_037334.1
NC_037335.1
...
NW...
etc.

To use the AGAT tool agat_sq_keep_annotation_from_fastaSeq.pl we need to prepare a fasta file containing only the chromosomes (https://www.biostars.org/p/454669/)

display unique numbers: sort -u 

to create .txt file containing chromosome number, start and stop sequence, use get_coordinates_for_all.sh

convert to standard format:
agat_convert_sp_gxf2gxf.pl --gff 8_test.gff

first add also introns
agat_sp_add_introns.pl --gff infile --out outFile



agat_sp_add_introns.pl --gff Bos_taurus.gff --out Bos_taurus_with_introns.gff
mam na to program ./add_introns.sh

vysosat jen introny a exony:
cat Bos_taurus_with_introns.gff | cut -f 3 | grep -e "intron" -e "exon" | sort -u

 cat *.txt | cut -f 2 | sort -u (kontrola ze mame jen introny a exony)

zobrazit jen chromosomy (plus jedno divne cislo je MT)
grep "^NC" Sus_scrofa_with_introns_simplified.txt | cut -f 1 | sort -u
jejich pocet:
 grep "^NC" Sus_scrofa_with_introns_simplified.txt | cut -f 1 | sort -u | wc

MT k odstraneni (u psa nic) - odstraneni provedeno manualne, bez skriptu:
Monodelphis_domestica NC_006299.1
Ornithorhynchus_anatinus NC_000891.1
Equus_caballus NC_001640.1
Ovis_aries  NC_001941.1
Sus_strofa NC_000845.1
Bos_taurus NC_006853.1
Rattus_norvegicus NC_001665.2
Felis_catus NC_001700.1
Mus_musculus NC_005089.1

filter_chromosome_names.py -> vyfiltruje na zaklade seznamu chtenych chromosomu data o chormosomech z filu jmeno, intron/exon, koordinaty do souboru data/chromosomes/\*chr_only.txt

    a=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`


cat filter_fasta_report.txt
Monodelphis_domestica (vačice, problémová, ale není to asi zas takový problém)
pocet exonu obsahujicich N: 93 (0.014279857569936754 %)
pocet intronu obsahujicich N: 50025 (8.615359709566365 %)

ostatní jsou v řádech setin procent, případně desetin (jeden případ)
nepovažuji za problematické odstranit takové množství
vytvořím tedy nové soubory které odmažou sekvence ve kterých jsou "N"


overeni uspesneho odstraneni N v souborech v data/ready_to_use/without_N:
grep -v "^[N]" \*.txt 
protoze jedine N se ma vyskytovat v nazvu chromosomu (zacatek radky, invertovany grep -v, tedy)

dale odstraneni duplikatu

pouzitelna data ulozena v data/ready_to_use/without_N/sorted_introns_exons/

# with open("data/ready_to_use_finally/sample/Sus_scrofa_sample_100MB.txt") as file:
#     line = file.readline()
#     print(line)