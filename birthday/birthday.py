#! /usr/bin/env python3

"""
In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary 
from a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the 
dictionary, and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names, your JSON 
file should keep getting bigger and bigger.

https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
"""

import json

BIRTHDAY_FILE = "birthdays.json"


def main():
    with open(BIRTHDAY_FILE) as f:
        birthdays = json.load(f)

    scientist = input("Enter the name of the scientist: ")
    if scientist in birthdays:
        print(f"{scientist} was born on {birthdays[scientist]}")
    else:
        new_birthday = input(f"I don't know that birthday! When was {scientist} born? ")
        birthdays[scientist] = new_birthday
        with open(BIRTHDAY_FILE, "w") as f:
            json.dump(birthdays, f, indent=2)


if __name__ == "__main__":
    main()
