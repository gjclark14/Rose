# http://rosalind.info/problems/dna/

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the
# respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

import sys
import os
from librose import Nucleotides


def main():

    f = open(sys.argv[1])
    tides = Nucleotides.Nucleotides()

    dna = f.read().rstrip()

    for d in dna:
        if d == 'A':
            tides.set_a(tides.get_a() + 1)
        elif d == 'C':
            tides.set_c(tides.get_c() + 1)
        elif d == 'G':
            tides.set_g(tides.get_g() + 1)
        elif d == 'T':
            tides.set_t(tides.get_t() + 1)

    print(tides.get_counts())

if __name__ == "__main__":
    main()
