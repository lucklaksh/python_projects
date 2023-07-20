from art import logo
import random
def guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,101)
    if input("choose a difficulty. Type 'easy' or 'hard': ").lower() == 'hard':
        chance = 5
    else:
        chance = 10
    iterated =0
    win =0
    while( chance >0):
        if(iterated!=0):
            print("Guess Again!")
        print(f"you have {chance} attempts remaining to guess the number.")
        num = int(input("Make a guess: "))
        if number== num:
            win =1
            # print(f"you got it! The answer was {num}.")
            break
        elif number > num:
            print("Too low.")
        else:
            print("Too high.")
        chance -= 1
        iterated=1
    if win ==1:
        print(f"you got it! you Win!\nThe answer was {num}.")
    else:
        print(f"You've run out of guesses, you Lose! \nThe answer was {number}.")




guessing_game()