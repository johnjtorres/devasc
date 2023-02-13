#! /usr/bin/env python3

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""


def main():
    while True:
        print()
        choices = get_choices()
        rps = rock_paper_scissors(*choices)
        if rps == 0:
            print("Player 1 wins!")
        elif rps == 1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

        new_game = input("Enter 'y' to play again: ")
        if new_game.lower() != "y":
            break


def get_choices():
    VALID_CHOICES = ("rock", "paper", "scissors")
    choices = []
    for i in range(2):
        while True:
            choices.append(input(f"Player {i+1} > Rock, Paper, or Scissors? ").lower())
            if choices[i] in VALID_CHOICES:
                break
            else:
                choices.pop()
    return choices


def rock_paper_scissors(choice1, choice2):
    win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if choice1 == choice2:
        return -1
    elif choice2 == win_conditions[choice1]:
        return 0
    else:
        return 1


if __name__ == "__main__":
    main()
