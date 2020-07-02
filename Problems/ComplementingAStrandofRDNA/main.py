# http://rosalind.info/problems/revc/

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.


import sys
import os


def main():

    f = open(sys.argv[1])

    # python sometimes isn't verbose enough
    # this reverses the string and removes whitespace
    dna = f.read().rstrip()[::-1]
    dna_rev_comp = ""

    for d in dna:
        if d == 'A':
            dna_rev_comp += 'T'
        elif d == 'C':
            dna_rev_comp += 'G'
        elif d == 'G':
            dna_rev_comp += 'C'
        elif d == 'T':
            dna_rev_comp += 'A'

    print(dna_rev_comp)

if __name__ == "__main__":
    main()
