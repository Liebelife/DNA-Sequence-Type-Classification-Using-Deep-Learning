#!/bin/bash
cat download_gff_fna.txt | while read line 
do
   wget -P data $line
   # do something with $line here
done