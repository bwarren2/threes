from board import Board

help_str = """
            Your options are:
            up (w): shift the board up.
            down (s): shift the board down.
            left (a): shift the board left.
            right (d): shift the board right.

            score (s): score the board and end the game.
            quit (q): quit the game.
            new (n): start a new game.
            help (h): print this list.
            """


def new_game():
    #setup
    print "                                      "
    print "                                      "
    print "                                      "
    print "            ### ################## ###"
    print "            ### Welcome to threes! ###"
    print "            ### ################## ###"
    print help_str
    board = Board(4)
    #game loop
    while True:

        print board
        choice = raw_input("(w, s, a, d, s, q, h?): ")

        if choice == 'w':
            board.shift('up')

        elif choice == 's':
            board.shift('down')

        elif choice == 'a':
            board.shift('left')

        elif choice == 'd':
            board.shift('right')

        elif choice == 'sc':
            print ""
            print "Your score: {0}".format(board.score())
            print ""

        elif choice == 'q':
            break

        elif choice == 'h':
            print help_str

        else:
            print help_str

if __name__ == '__main__':
    new_game()
