def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return("FizzBuzz")
    elif number % 5 == 0:
        return("Buzz")
    elif number % 3 == 0:
        return("Fizz")
    else:
        return(number)

def main():
    for a in range(1, 101):
        print(fizzbuzz(a))
    return

if __name__ == '__main__':
    main()
