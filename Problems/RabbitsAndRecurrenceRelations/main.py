# http://rosalind.info/problems/dna/

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the
# respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

import sys
import os


def main():

    f = open(sys.argv[1])

    fin = f.readline().split()
    n = int(fin[0])
    k = int(fin[1])

    rabbits = [1, 1+k]

    i = 2
    while i < n:
        rabbits.append(rabbits[i-1] + k*rabbits[i-2])
        i += 1


    # for whatever reason we don't actually care about the last calculated month
    print(rabbits[-2])


if __name__ == "__main__":
    main()
