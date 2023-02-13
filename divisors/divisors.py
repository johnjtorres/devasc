#! /usr/bin/env python3

"""
Create a program that asks the user for a number and then prints out a list of 
all the divisors of that number. (If you don’t know what a divisor is, it is a 
number that divides evenly into another number. For example, 13 is a divisor of 
26 because 26 / 13 has no remainder.)

https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""


def main():
    while True:
        try:
            num = int(input("Number: "))
        except ValueError:
            continue
        else:
            break
    print("Divisors:", *(divisors(num)))


def divisors(num):
    return [n for n in range(1, num + 1) if num % n == 0]


if __name__ == "__main__":
    main()
