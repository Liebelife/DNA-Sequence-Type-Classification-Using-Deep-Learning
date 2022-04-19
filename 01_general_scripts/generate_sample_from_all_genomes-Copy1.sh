#!/bin/bash

# takes an argument (number of lines to be taken from each file)

names_path=/home/lieberze/DP/data/
path=/home/lieberze/DP/data/ready_to_use/without_N/sorted_introns_exons_intergenic/

N_max=$1

rm -f ${path}samples/Sample_of_all_genomes_large_${N_max}.txt
touch ${path}samples/Sample_of_all_genomes_large_${N_max}.txt

for i in ${names_path}/*.fna; do
    name=`echo $i | rev |cut -d "/" -f 1 | rev | cut -d "." -f 1`
    cat ${path}${name}_introns_exons_intergenic_no_duplicates_without_N.txt | head -${N_max} >> ${path}samples/Sample_of_all_genomes_large_${N_max}.txt 
done