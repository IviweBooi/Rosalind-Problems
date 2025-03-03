from NucleotideCount import validate_s


def r_complement(s):
    """This function returns a reverse complement of a DNA sequence s"""
    complements = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    results = ''
    for nucleotide in s:
        for key, value in complements.items():
            if nucleotide == key:
                results += value
    return results[-1::-1]  # reverse the results


def main():
    s = input("enter a DNA string of length at most 1000 bp:\n")
    validated_s = validate_s(s)
    print(r_complement(validated_s))


if __name__ == '__main__':
    main()



