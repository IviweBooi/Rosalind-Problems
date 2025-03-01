def validate_s(string):
    """This function validates whether a given string is a DNA string
       with valid nucleotide bases and returns the string if valid or returns False if not"""
    nucleotides = ['A', 'C', 'G', 'T']
    for base in string.upper():
        if base not in nucleotides:
            return False
    return string.upper()


def count_nucleotides(string):
    """This function returns four integers (separated by spaces)
       counting the respective number of times that the symbols
       'A', 'C', 'G', and 'T' occur in s."""
    if type(string) is not str:
        return "Invalid DNA seq!"
    else:
        dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nucleotide in string:
            dic[nucleotide] += 1  # increment the base element in the dictionary

        return " ".join(str(value) for value in dic.values())


def main():
    s = input("A DNA string s of length at most 1000 nt:\n")
    validated_s = validate_s(s)
    print(count_nucleotides(validated_s))


if __name__ == "__main__":
    main()



