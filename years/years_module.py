import datetime


def years(age):
    return_date = datetime.datetime.now().year + 100 - age
    return (return_date)


def main():
    age = int(input('How old are you? '))
    name = input('What is your name? ')
    print(name + ", you will be 100 years old in: " + str(years(age)))
    return


if __name__ == '__main__':
    main()
