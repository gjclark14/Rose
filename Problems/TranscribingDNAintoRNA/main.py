# http://rosalind.info/problems/rna/

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

import sys
import os


def main():

    f = open(sys.argv[1])

    dna = f.read().rstrip()

    rna = ""

    for d in dna:
        if d == 'T':
            rna += 'U'
        else:
            rna += d

    print(rna)

if __name__ == "__main__":
    main()
