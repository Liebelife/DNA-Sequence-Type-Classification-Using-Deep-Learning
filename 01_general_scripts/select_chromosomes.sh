#!/bin/bash

for i in data/with_introns/*.txt; do
	a=`echo $i | cut -d "/" -f 3 | cut -d "." -f 1`
	grep "^NC" $i | cut -f 1 | sort -u > data/chromosomes/${a}_chr.txt
done