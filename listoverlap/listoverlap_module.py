from random import randint




def listoverlap(list1 = [randint(1, 100) for i in range(0, randint(1, 100))], list2 = [randint(1, 100) for i in range(0, randint(1, 100))]):
    return list(set(list1).intersection(set(list2)))



def main():
    print(listoverlap())
    return


if __name__ == '__main__':
    main()
