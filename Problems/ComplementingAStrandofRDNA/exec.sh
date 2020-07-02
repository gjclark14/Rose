#!/bin/bash

rm -fv out.txt
python3 $1 $2 > out.txt
rm -fv rosalind_revc.txt
