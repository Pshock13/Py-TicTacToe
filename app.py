#global variables
boardSpot = [" "," "," "," "," "," "," "," "," "]
randTurn = randint(1,2)
player1 = ""
player2 = ""

#function logic below
print_board()
whoseTurn()


#defined functions
#whose turn prints out who goes first and assigns them to ttheir letter
def whoseTurn(randTurn):
    if randTurn == 1:
        print("X goes first")
        player1 = "X"
        player2 = "O"
    else:
        print("O goes first")
        player1 = "O"
        player2 = "X"



#this function prints the status of the board 
def print_board():
    print("Decide who wants to be X or O!")
    print(".................")
    print(boardSpot[0] + "|" + boardSpot[1] + "|" + boardSpot[2])
    print(".................")
    print(boardSpot[3] + "|" + boardSpot[4] + "|" + boardSpot[5])
    print(".................")
    print(boardSpot[6] + "|" + boardSpot[7] + "|" + boardSpot[8])
    print(".................")