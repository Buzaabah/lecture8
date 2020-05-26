def main():
    raw_string = input('Enter String: ')
    new_string = remove_non_number(raw_string)
    print(new_string)

def remove_non_number(str):
    only_numbers = ''

    for char in str:
        if char.isdigit():
            only_numbers = only_numbers + char
    return only_numbers



    #example = "Hi mom😊"

    # example of length function
    #length = len(example)
    #print(length)  # prints 6

    # example of getCharAt
    #first = example[0]
    #print(first)  # prints 'H'

    # loop that prints letters one-by-one
    #for i in range(len(example)):
        #ch = example[i]
        #print(i, ch)




if __name__ == '__main__':
    main()