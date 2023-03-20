import random
import player

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
    if 0 <= int(move_input) <= 8:
        boardSpot[int(move_input)] = p.symbol
        # switch players her after a move is made
    else:
        make_a_move(p, input("Please submit a move 0-8 "))
    print_board()


def play_tic_tac_toe():
    # determines if X or O goes first
    if rNum <= 5:
        current_player = px
    else:
        current_player = po

    # lets players know who goes first
    print(current_player.name + " will go first!")
    for i in range(1, 10):
        # 3 prints to help us know what iteration we are on
        print("")
        print("Turn: " + str(i))
        print("_______")
        # get the player's move input
        move_input = int(input(current_player.full + ", where would you like to move? "))
        # check if number is between 0 and 8
        # (need to also check that a number and not a string was entered in the future)
        if 0 <= move_input <= 8:
            boardSpot[move_input] = current_player.symbol
            # switch players after a successful turn
            if current_player == px:
                current_player = po
            else:
                current_player = px
        else:
            # if a bad input was entered, give player a chance to enter proper move.
            # Also, need to not move onto the next iteration until a proper move has been entered
            move_input = input("Please submit a move 0-8 ")
        print_board()


play_tic_tac_toe()
