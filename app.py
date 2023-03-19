import random

# global variables
boardSpot = ["#","#","#","#","#","#","#","#","#"]
randTurn = random.randint(1,10)
playerX = ""
playerO = ""
player1 = ""
player2 = ""

# this function prints the status of the board 
def print_board():
    print("  L|M|R")
    print("U " + boardSpot[0] + "|" + boardSpot[1] + "|" + boardSpot[2])
    print("M " + boardSpot[3] + "|" + boardSpot[4] + "|" + boardSpot[5])
    print("B " + boardSpot[6] + "|" + boardSpot[7] + "|" + boardSpot[8])

# this function gets the player names and assigns them to X or O
def XOplayer(pX, pO):
    
    pX = input("Decide: who wants to be X? Enter your name: \n")
    playerX = pX
    print(playerX + " will be X!")
    pO = input("Player 2 will be O. Enter your name: \n")
    playerO = pO
    print(playerO + " will be O!")

XOplayer(playerX, playerO)

# using a random number determines if X or O goes first
def whoseTurn(randTurn):
    tempvar = ""
    if randTurn <= 5:
        tempvar = "X"
    else:
        tempvar = "O"

    return tempvar

firstPlayer = whoseTurn(randTurn)

if firstPlayer == "X":
    player1 = "X"
    player2 = "O"
else: 
    player1 = "O"
    player2 = "X"

# lets players know who goes first
print(firstPlayer + " will go first!")

def play_tic_tac_toe(p1, p2, FP):
    for i in range(1,10):
        answers = {
            1: ,

        }
        if i % 2 > 0:


        print_board()
        

        
play_tic_tac_toe(player1, player2, firstPlayer)