#!/bin/bash

for i in data/*.gff; do
	name=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`
	python3 remove_duplicated_lines.py $name
done
