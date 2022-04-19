#!/bin/bash

for i in data/*.fna; do
    name=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`
    address=data/ready_to_use/without_N/
    cat ${address}${name}_no_duplicates_without_N.txt ${address}${name}_intergenic_no_duplicates_without_N.txt > ${address}${name}_introns_exons_intergenic_no_duplicates_without_N.txt
    sort -k1,1r -k3,3n ${address}${name}_introns_exons_intergenic_no_duplicates_without_N.txt > ${address}/sorted_introns_exons_intergenic/${name}_introns_exons_intergenic_no_duplicates_without_N.txt
done
