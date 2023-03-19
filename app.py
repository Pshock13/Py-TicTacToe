import random

# global variables
boardSpot = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
randTurn = random.randint(1, 10)
px = ""
po = ""


# this function prints the status of the board
def print_board():
    print("  L|M|R")
    print("U " + boardSpot[0] + "|" + boardSpot[1] + "|" + boardSpot[2])
    print("M " + boardSpot[3] + "|" + boardSpot[4] + "|" + boardSpot[5])
    print("B " + boardSpot[6] + "|" + boardSpot[7] + "|" + boardSpot[8])


# this gets the player names and assigns them to X or O
px = input("Decide who wants to be X? Enter your name: \n")
print(px + " will be X!")
po = input("Player 2 will be O. Enter your name: \n")
print(po + " will be O!")

px += "(X)"
po += "(O)"

# using a random number determines if X or O goes first
if randTurn <= 5:
    player1 = px
    player2 = po
else:
    player1 = po
    player2 = px

# lets players know who goes first
print(player1 + " will go first!")


def make_a_move(x, o):
    print("move on " + x)
    if x == "ul":
        boardSpot[0] = o
    elif x == "um":
        boardSpot[1] = o
    elif x == "ur":
        boardSpot[2] = o
    elif x == "ml":
        boardSpot[3] = o
    elif x == "mm":
        boardSpot[4] = o
    elif x == "mr":
        boardSpot[5] = o
    elif x == "bl":
        boardSpot[6] = o
    elif x == "bm":
        boardSpot[7] = o
    elif x == "br":
        boardSpot[8] = o
    else:
        make_a_move(input("Please submit a proper move "), o)


def play_tic_tac_toe(p1, p2):
    for i in range(1, 10):
        # answers = {
        #     1:,
        #
        # }
        # odd iteration = player1's turn while even iterate is player2's turn
        if i % 2 > 0:
            make_a_move(input(player1 + " where would you like to move? "), "X")
        else:
            make_a_move(input(player2 + " where would you like to move? "), "O")

        print_board()


# player1 and firstPlayer and one and the same; dropping firstPlayer
# play_tic_tac_toe(player1, player2, firstPlayer)
play_tic_tac_toe("X", "O")
