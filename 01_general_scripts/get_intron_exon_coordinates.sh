#!/bin/bash


# greps word "exon" and "intron" in .gff file with added exons (passed as an argument when calling this script)
# cuts the 1st, 3rd, 4th and 5th column in grepped line
# these are gene number, annotation (intron/exon) the start and stop of intron/exon coordinates
# saves the exon coordinates to a new file $1_exons.txt

a=`echo $1 | cut -d "/" -f 3 | cut -d "." -f 1`
cat $1 | cut -f 1,3,4,5 | grep -e "intron" -e "exon" > data/with_introns/${a}_simplified.txt
