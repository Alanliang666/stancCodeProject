"""
File: complement.py
Name: Alan
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Run the complement function with various DNA strand
    Prints the complement results to the console
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    : param dna : str, user can enter any DNA strand (e.g. A, T, C, G)
    : return : str, return the result complement each DNA strand or an error message if empty
    Finds the complement of a DNA strand
    """
    ans = ''
    if dna == '':
        return 'DNA strand is missing'
    else:
        for i in range(len(dna)):
            if dna[i] == 'A':
                ans += 'T'
            elif dna[i] == 'T':
                ans += 'A'
            elif dna[i] == 'G':
                ans += 'C'
            elif dna[i] == 'C':
                ans += 'G'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
