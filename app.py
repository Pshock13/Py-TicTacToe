import random
import player
import os

# global variables
boardSpot = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
rNum = random.randint(1, 10)  # set a random number for use later


# this function prints the status of the board
def print_board():
    print(boardSpot[0] + "|" + boardSpot[1] + "|" + boardSpot[2])
    print(boardSpot[3] + "|" + boardSpot[4] + "|" + boardSpot[5])
    print(boardSpot[6] + "|" + boardSpot[7] + "|" + boardSpot[8])


# this gets the player names and assigns them to X or O
px = player.Player(input("Who will be X? Enter your name: ").title(), "X")
po = player.Player(input("Who will be O? Enter your name: ").title(), "O")
print(px.name + " will be X! " + po.name + " will be O!")


def make_a_move(p, move_input):
    # check that input is a number
    if move_input.isdigit():
        # check that the number is between 0 and 8
        if 0 <= int(move_input) <= 8:
            # check that spot has not been used yet
            if boardSpot[int(move_input)] == "*":
                boardSpot[int(move_input)] = p.symbol
            else:
                make_a_move(p, input("Please submit a location that has not been used yet "))
        else:
            make_a_move(p, input("Please submit a number between 0-8 "))
    else:
        make_a_move(p, input("Please submit a number between 0-8 "))


def switch_player(p):
    if p == px:
        return po
    else:
        return px


def play_tic_tac_toe():
    # determines if X or O goes first
    if rNum <= 5:
        current_player = px
    else:
        current_player = po

    # lets players know who goes first
    print(current_player.name + " will go first!")
    for i in range(1, 10):
        os.system("cls")
        # x2 prints to help us know what iteration we are on
        print("Turn: " + str(i))
        print("------")
        print_board()
        # get the player's move input
        make_a_move(current_player, input(current_player.full + ", where would you like to move? "))
        current_player = switch_player(current_player)


play_tic_tac_toe()
