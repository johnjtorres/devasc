#! /usr/bin/env python3

"""
Ask the user for a string and print out whether this string is a palindrome or 
not. (A palindrome is a string that reads the same forwards and backwards.)

https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""


def main():
    phrase = input("Enter a word or phrase to check if it is a palindrome: ")
    if is_palindrome(phrase):
        print("That is a palindrome!")
    else:
        print("That is not a palindrome.")


def is_palindrome(phrase):
    only_alpha = [p.lower() for p in phrase if p.isalpha()]
    return only_alpha == only_alpha[::-1]


if __name__ == "__main__":
    main()
