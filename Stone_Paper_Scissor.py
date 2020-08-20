"""stone paper scissor game in python"""
import random


def stone_paper_scissor():
    print("rules of the game are \n" +
          "rock vs paper -> paper wins \n" +
          "rock vs scissor -> rock wins \n" +
          "scissor vs paper -> scissor wins \n" +
          "winner gets 5 points")

    # initialise scores of user and computer to 0
    user_score = 0
    computer_score = 0
    total_matches_played = 0
    while True:
        print("Please choose any one \n 1. rock \n 2. paper \n 3. scissor \n")
        # take user's input
        user_choice = int(input("user_choice:"))

        # check if user has entered invalid choice
        while user_choice < 1 or user_choice > 3:
            print("please enter a valid input:")
            user_choice = int(input())

        # initialise the values corresponding to user's choice
        if user_choice == 1:
            user_choice_name = "Rock"
        elif user_choice == 2:
            user_choice_name = "Paper"
        else:
            user_choice_name = "scissor"

        print(f"user's choice is {user_choice_name} \n now let the computer choose")

        # computer will randomly choose any value between the range provided using random
        # in this case the range is between 1 to 3
        computer_choice = random.randint(1, 3)

        # if there is a tie computer will again randomly pick another number till there is no tie
        while computer_choice == user_choice:
            computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice_name = 'Rock'
        elif computer_choice == 2:
            computer_choice_name = 'Paper'
        else:
            computer_choice_name = 'Scissor'

        print(f"computer's choice is {computer_choice_name}")
        print(f"{user_choice_name} vs {computer_choice_name}")

        # winning condition
        if computer_choice == 1 and user_choice == 2 or computer_choice == 2 and user_choice == 1:
            print("Paper wins", end="")
            result = "Paper"
        elif computer_choice == 1 and user_choice == 3 or computer_choice == 3 and user_choice == 1:
            print("Rock wins", end="")
            result = "Rock"
        else:
            print("Scissor wins", end="")
            result = "Scissor"

        # final result, whether user won or computer
        if result == user_choice_name:
            user_score = user_score + 5
            print("User won")

        else:
            computer_score = computer_score + 5
            print("Computer won")

        print(f"score of user so far=> {user_score} \n" +
              f"score of computer so far=> {computer_score}")

        # to count the total number of matches played so far
        total_matches_played += 1

        print(" Do you want to play again? Y or N ")
        user_decision = input()

        while user_decision not in ['Y', 'y', 'n', 'N']:
            print("please enter a valid choice:")
            user_decision = input()

        # if user says no come out of the loop and the game stops
        if user_decision == 'N' or user_decision == 'n':
            break

    # while loop ends here

    print(f"Total matches played are : {total_matches_played}")
    print(f"final score of user => {user_score} \n" +
          f"final score of computer => {computer_score} \n")

    if user_score > computer_score:
        print("USER WON")
    elif user_score == computer_score:
        print("TIE")
    else:
        print("COMPUTER WON")

    print("Thanks for playing the game")


# stone_paper_scissor()

""" alternative way to create the game """


def rock_paper_scissor():
    print("rules of the game are \n" +
          "rock vs paper -> paper wins \n" +
          "rock vs scissor -> rock wins \n" +
          "scissor vs paper -> scissor wins \n" +
          "winner gets 5 points")

    # initialise scores of user and computer to 0
    user_score = 0
    computer_score = 0
    total_matches_played = 0
    list_of_game_names = ['Rock', 'Paper', 'Scissor']

    print("PLease enter your name:")
    user_name = input()

    while True:
        print(f"Hi {user_name} please enter your choice \n" +
              "1. rock \n 2. paper \n 3. scissor \n")
        user_choice = int(input())

        while user_choice not in [1, 2, 3]:
            user_choice = int(input(f"{user_name} please enter a valid choice"))

        choice = user_choice
        choice_name = list_of_game_names[choice - 1]

        if user_choice == 1:
            user_choice_name = choice_name
        elif user_choice == 2:
            user_choice_name = choice_name
        else:
            user_choice_name = choice_name

        print(f"{user_name} your choice is {user_choice_name}")
        print("Now COMPUTER'S turn")

        computer_choice = random.randint(1, 3)

        while computer_choice == user_choice:
            computer_choice = random.randint(1, 3)

        choice = computer_choice
        choice_name = list_of_game_names[choice - 1]

        if computer_choice == 1:
            computer_choice_name = choice_name
        elif computer_choice == 2:
            computer_choice_name = choice_name
        else:
            computer_choice_name = choice_name

        print(f"computer's choice is {computer_choice_name} \n")

        # winning condition
        if computer_choice == 1 and user_choice == 2 or computer_choice == 2 and user_choice == 1:
            print("Paper wins \n", end="")
            result = "Paper"
        elif computer_choice == 1 and user_choice == 3 or computer_choice == 3 and user_choice == 1:
            print("Rock wins \n", end="")
            result = "Rock"
        else:
            print("Scissor wins \n", end="")
            result = "Scissor"

        # final result, whether user won or computer
        if result == user_choice_name:
            user_score = user_score + 5
            print(f"Congrats {user_name.upper()} you won this time \n ")

        else:
            computer_score = computer_score + 5
            print(f"COMPUTER won")

        print(f"score of {user_name} so far=> {user_score} \n" +
              f"score of computer so far=> {computer_score}")

        # to count the total number of matches played so far
        total_matches_played += 1

        print(" Do you want to play again? Y or N ")
        user_decision = input()

        while user_decision not in ['Y', 'y', 'n', 'N']:
            print("please enter a valid choice:")
            user_decision = input()

        # if user says no come out of the loop and the game stops
        if user_decision == 'N' or user_decision == 'n':
            break

    # while loop ends here

    print(f"Total matches played are : {total_matches_played}")
    print(f"final score of user => {user_score} \n" +
          f"final score of computer => {computer_score} \n")

    if user_score > computer_score:
        print(f"{user_name.upper()} YOU WON !!!")
    elif user_score == computer_score:
        print("TIE")
    else:
        print("COMPUTER WON !!!")

    print("Thanks for playing the game")


# rock_paper_scissor()