#!/bin/bash

for i in data/with_introns/*.gff; do
	./get_intron_exon_coordinates.sh $i
done
