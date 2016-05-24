import random
import string


def passwordgen():
    list_c = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    passw = []

    for i in range(2):
        passw.append(random.choice(list_c))
        passw.append(random.choice(string.digits))
        passw.append(random.choice(string.ascii_lowercase))
        passw.append(random.choice(string.ascii_uppercase))
    random.shuffle(passw)
    passw_return = ''.join(passw)
    return(passw_return)


def main():
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
