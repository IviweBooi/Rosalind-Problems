def count_pairs(n, k):
    """This function takes the total number of rabbit pairs that will be present after n
    months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
    rabbit pairs.
    :param n: months
    :param k: rabbit pairs"""

    pairs_no = {1: 1, 2: 1}  # keys represent months and value represents the number of pairs
    # if the number of months is greater than 2
    if n > 2:
        m = 2  # month counter
        for i in range(n+1):
            # total pairs for the next month is equal
            # to the previous original pair plus their k pairs of new offsprings.
            pairs_no[m+1] = pairs_no[m] + pairs_no[m-1]*k
            m += 1

    return pairs_no[n]


def main():
    raw_input = input("Enter the number of months and rabbit pairs separated my a space:\n")
    # input processing
    processed_input = (raw_input.strip()).split(" ")
    n = int(processed_input[0])
    k = int(processed_input[1])
    print(count_pairs(n, k))


if __name__ == '__main__':
    main()
