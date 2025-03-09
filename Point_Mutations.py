def hamming_distance(s, t):
    """This function takes 2 DNA seqs of equal length,
       and return the hamming distance (number of corresponding symbols that differ in s and t)."""
    counter = 0
    for i in range(len(s)):
        # if the bases in the current index are not the same, increment counter by 1.
        if s[i] != t[i]:
            counter += 1

    return counter


def main():
    s = input("Enter the first DNA seq:\n")
    t = input("Enter the second DNA seq:\n")
    print(hamming_distance(s, t))


if __name__ == '__main__':
    main()
