from NucleotideCount import validate_s


def dna_to_rna(s):
    """This function returns RNA version of the provided DNA seq"""
    return s.replace("T", "U")


def main():
    s = input("Enter the DNA seq:\n")
    validated_s = validate_s(s)
    print(dna_to_rna(validated_s))


if __name__ == '__main__':
    main()
