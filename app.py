ul = "  *  "
um = "  *  "
ur = "  *  "

ml = "  *  "
mm = "  *  "
mr = "  *  "

bl = "  *  "
bm = "  *  "
br = "  *  "


def print_board():
    print(".................")
    print(ul + "|" + um + "|" + ur)
    print(".................")
    print(ml + "|" + mm + "|" + mr)
    print(".................")
    print(bl + "|" + bm + "|" + br)
    print(".................")


print_board()
whoseTurn = input("Who is starting? (X or O?) ").upper()

move = input(whoseTurn + "'s turn. Where would you like to move? ")
if move == "ul":
    ul = "  " + whoseTurn + "  "
elif move == "um":
    um = "  " + whoseTurn + "  "
elif move == "ur":
    ur = "  " + whoseTurn + "  "
elif move == "ml":
    ml = "  " + whoseTurn + "  "
elif move == "mm":
    mm = "  " + whoseTurn + "  "
elif move == "mr":
    mr = "  " + whoseTurn + "  "
elif move == "bl":
    bl = "  " + whoseTurn + "  "
elif move == "bm":
    bm = "  " + whoseTurn + "  "
elif move == "br":
    br = "  " + whoseTurn + "  "

print_board()
