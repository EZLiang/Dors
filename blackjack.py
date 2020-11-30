from random import randint
from time import sleep

suits = ["♣", "♥", "♠", "♦"]
ranks = ["A","2","3","4","5","6","7","8","9","J","Q","K"]

game_running = True
win_string = ""

def init():
    global player_hand
    global computer_hand
    player_hand = []
    computer_hand = []
    for i in range(2):
        player_hand.append(ranks[randint(0,11)]+suits[randint(0,3)])
        computer_hand.append(ranks[randint(0,11)]+suits[randint(0,3)])

def get_hand_sum(hand):
    running_sum = 0
    for i in range(len(hand)):
        card_rank = (hand[i])[0]
        if card_rank == "A":
            running_sum += 1
        elif card_rank == "J" or card_rank == "Q" or card_rank == "K":
            running_sum += 10
        else:
            running_sum += int(card_rank)

    return running_sum

def check_hand_valid(hand):
    if get_hand_sum(hand) > 21:
        return "Busted..."
    if get_hand_sum(hand) == 21:
        return "Blackjack!"
    if get_hand_sum(hand) < 21:
        return "Current Total: "+str(get_hand_sum(hand))


def draw_card():
    return ranks[randint(0, 11)] + suits[randint(0, 3)]


while game_running == True:
    init()
    while True:
        print("Player Hand:")
        print(player_hand)
        while True:
            action = input("Hit/Stand: ")
            if action.lower() == "hit":
                drawn_card = draw_card()
                player_hand.append(drawn_card)
                print("Drawn Card:",drawn_card)
                break
            elif action.lower() == "stand":
                break
            else:
                print("Not a command. Try again.")
        print(check_hand_valid(player_hand))
        if check_hand_valid(player_hand) == "Busted...":
            win_string = "The computer wins! Better luck next time..."
            break
        elif check_hand_valid(player_hand) == "Blackjack!":
            win_string = "You won! Nice job!"
            break
        else:
            ...

        sleep(0.5)
        print("\n")

        print("Computer Hand:")
        print(computer_hand)
        drawn_card = draw_card()
        if get_hand_sum(computer_hand) < 17:
            randomizer = randint(1,12)
            if randomizer == 12:
                print("Stand")
            else:
                print("Hit")
                computer_hand.append(drawn_card)
                print("Drawn Card:", drawn_card)
        elif get_hand_sum(computer_hand) >= 17:
            randomizer = randint(1,20)
            if randomizer == 20:
                print("Stand")
            else:
                print("Hit")
                computer_hand.append(drawn_card)
                print("Drawn Card:", drawn_card)
        print(check_hand_valid(computer_hand))
        if check_hand_valid(computer_hand) == "Busted...":
            win_string = "The player wins! The computer should get smarter..."
            break
        elif check_hand_valid(computer_hand) == "Blackjack!":
            win_string = "The computer won! Better luck next time..."
            break
        else:
            ...

        sleep(0.5)
        print("\n")


    print(win_string)
    while True:
        replay = input("Would you like to play again (Y/N)? ")
        if replay.lower() == "y":
            print()
            break
        elif replay.lower() == "n":
            game_running = False
            break
        else:
            print("Not an option. Try again.")




