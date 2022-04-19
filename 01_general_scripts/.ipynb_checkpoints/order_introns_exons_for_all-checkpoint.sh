#!/bin/bash

command=$1
for i in data/*.fna; do
	name=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`
	address=data/ready_to_use/without_N/
	sort -k1,1r -k3,3n ${address}${name}_no_duplicates_without_N.txt > ${address}/sorted_introns_exons/${name}_no_duplicates_without_N_sorted.txt
done
