import string


def palindrome(str):
    str = str.lower()
    test_str = ''.join(str.split())
    temp = []
    for c in test_str:
        temp.append(c)
    temp.reverse()
    test_str_reversed = ''.join(temp)
    if test_str == test_str_reversed:
        return(True)
    else:
        return(False)


def main():
    pal_str = input('Gimme a string, human! ')
    print(palindrome(pal_str))
    return


if __name__ == '__main__':
    main()
