from random import randint

a = randint(1, 100)
a_list = []
b_list = []
for i in range(0, a):
    a_list.append(randint(1, 100))
    b_list.append(randint(1, 100))


def listoverlap(list1, list2):
    c = set(list1).intersection(set(list2))
    return(list(c))


def main():
    print(listoverlap(a_list, b_list))
    return


if __name__ == '__main__':
    main()
