spots = ["  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  "]


def print_board():
    print("     L     M     R  ")
    print("U |" + spots[0] + "|" + spots[1] + "|" + spots[2])
    print("  ..................")
    print("M |" + spots[3] + "|" + spots[4] + "|" + spots[5])
    print("  ..................")
    print("B |" + spots[6] + "|" + spots[7] + "|" + spots[8])
    print("  ..................")


player = 'X'


def make_a_move(p):
    move = input(p + "'s turn. Where would you like to move? ")

    if move == "ul":
        spots[0] = "  " + p + "  "
    elif move == "um":
        spots[1] = "  " + p + "  "
    elif move == "ur":
        spots[2] = "  " + p + "  "
    elif move == "ml":
        spots[3] = "  " + p + "  "
    elif move == "mm":
        spots[4] = "  " + p + "  "
    elif move == "mr":
        spots[5] = "  " + p + "  "
    elif move == "bl":
        spots[6] = "  " + p + "  "
    elif move == "bm":
        spots[7] = "  " + p + "  "
    elif move == "br":
        spots[8] = "  " + p + "  "

    print_board()
    if p == "X":
        p = "O"
    else:
        p = "X"
    return p


i = 0
while i < 9:
    player = make_a_move(player)
    i += 1
