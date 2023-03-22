import random
import player
import os

os.system('cls')
# global variables
boardSpot = ["", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
rNum = random.randint(1, 10)  # set a random number for use later
win_cond = {
    {"1", "2", "3"},
    {"4", "5", "6"},
    {"7", "8", "9"},
    {"1", "5", "9"},
    {"3", "5", "7"},
    {"7", "4", "1"},
    {"8", "5", "2"},
    {"9", "6", "3"},
}


# this function prints the status of the board
def print_board():
    print(boardSpot[7] + "|" + boardSpot[8] + "|" + boardSpot[9])
    print(boardSpot[4] + "|" + boardSpot[5] + "|" + boardSpot[6])
    print(boardSpot[1] + "|" + boardSpot[2] + "|" + boardSpot[3])


# this gets the player names and assigns them to X or O
px = player.Player(input("Who will be X? Enter your name: ").title(), "X")
po = player.Player(input("Who will be O? Enter your name: ").title(), "O")
print(px.name + " will be X! " + po.name + " will be O!")


def make_a_move(p, move_input):
    # check that input is a number
    if move_input.isdigit():
        # check that the number is between 0 and 8
        if 1 <= int(move_input) <= 9:
            # check that spot has not been used yet
            if boardSpot[int(move_input)] == "*":
                boardSpot[int(move_input)] = p.symbol
            else:
                make_a_move(p, input("Please submit a location that has not been used yet "))
        else:
            make_a_move(p, input("Please submit a number between 1-9 "))
    else:
        make_a_move(p, input("Please submit a number between 1-9 "))


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
    for i in range(1, 10):
        os.system("cls")
        # x2 prints to help us know what iteration we are on
        print("Turn: " + str(i))
        print("-----")
        print_board()
        # get the player's move input
        make_a_move(current_player, input(current_player.full + ", where would you like to move? "))
        current_player = switch_player(current_player)


play_tic_tac_toe()
