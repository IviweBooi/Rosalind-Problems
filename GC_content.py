def gc_content(f):
    """This function takes at most 10 DNA strings
     in FASTA format (of length at most 1 kbp each)
     as s and returns the ID of the string having the
     highest GC-content, followed by the GC-content of that string."""
    user_ids = {}
    long_string = (f.read()).replace("\n", "")  # remove all the newlines in the file to make a long string
    string_list = ((long_string.replace('>', ' >')).strip()).split(" ")  # split the string so you have a list

    for i in string_list:
        user_ids[i[1:(i.index('_'))+5:]] = i[(i.index('_'))+5::]  # associating user_id with its sequence

    highest = 0.0  # initial highest GC content
    counter = 0
    complete_info = {}
    for key, value in user_ids.items():
        for base in value:
            if base == "G" or base == "C":
                counter += 1
        if (counter/len(value))*100 > highest:
            highest = (counter/len(value))*100
            complete_info = {key: round(highest, 6)}  # key with the highest GC content
        counter = 0  # reset counter for the next iteration
    for key, value in complete_info.items():
        results = f'{key} \n{value}'
    return results


def main():
    infile = input("Enter the file you wish to open:\n")
    with open(infile, 'r') as f:
        print(gc_content(f))


if __name__ == "__main__":
    main()
