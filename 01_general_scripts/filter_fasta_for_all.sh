#!/bin/bash

command=$1
for i in data/*.fna; do
	name=`echo $i | cut -d "/" -f 2 | cut -d "." -f 1`
	echo $name
	python3 $command $name
done
