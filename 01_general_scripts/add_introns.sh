#!/bin/bash

for i in data/*.gff; do
	a=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`
	agat_sp_add_introns.pl --gff $i --out data/with_introns/${a}_with_introns.gff
done
