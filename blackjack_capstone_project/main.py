from art import logo
import random
print(logo)

cards =[ 11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    player = []
    delear =[]
    player.append(random.choice(cards))
    dealer1 = random.choice(cards)
    player.append(random.choice(cards))
    dealer2 = random.choice(cards)
    delear.append(dealer1)
    delear.append(dealer2)

    print(f"Your cards: {player}")
    print(f"Computer's first card: {dealer1}")
    another_card ='y'
    while(True):
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'n':
            break
        draw = random.choice(cards)
        player.append(draw)
        print(f"Your cards: {player}")
        if 11 in player and sum(player)>21:
            ind = player.index(11)
            player[ind]=1
        if sum(player)>21:
            print("it's a Bust!\n You Lose!")
            continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if continue_game =='y':
                blackjack()
                return
            else:
                return
    total_player = sum(player)
    print(f"your final hand: {player}")

    delear_total= sum(delear)
    while(delear_total < 17):
        draw = random.choice(cards)
        delear.append(draw)
        if 11 in delear and sum(delear)>21:
            ind = delear.index(11)
            delear[ind]=1
        delear_total = sum(delear)
        if delear_total >21:
            print("it's a Bust!\n You Win!")
            continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if continue_game =='y':
                blackjack()
                return
            else:
                return
    print(f"computer's final hand: {delear}")
    if(total_player == delear_total):
        print("It's a Draw!")
    elif total_player> delear_total:
        print("You win!")
    else:
        print("You Lose!")
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continue_game == 'y':
        blackjack()
        return
    else:
        return


blackjack()