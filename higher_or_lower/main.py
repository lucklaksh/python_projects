from art import logo, vs
import random
from game_data import data

def game():
    print(logo)
    game_list = data
    a = random.choice(game_list)
    game_list.remove(a)
    b = random.choice(game_list)
    game_list.remove(b)
    win = 1
    score = 0
    while(True):
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if(choice == 'a'):
            if (a['follower_count'] > b['follower_count']):
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                break
        elif(choice == 'b'):
            if (b['follower_count'] > a['follower_count']):
                print(f"You're right! Current score: {score}")
                score += 1
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                break
        else:
            print('Invalid choice!')
            break
        a = b
        b = random.choice(game_list)
        game_list.remove(b)

game()
