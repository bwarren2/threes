# -*- coding: utf-8 -*-
from board import Board

help_str = """
            Your options are:
            up (u): shift the board up.
            down (d): shift the board down.
            left (l): shift the board left.
            right (r): shift the board right.

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
        choice = raw_input("(u, d, l, r, s, q, n, h?): ")

        if choice == 's':
            raise Exception

        elif choice == 'q':
            break

        elif choice == 'n':
            raise Exception

        elif choice == 'h':
            print help_str

        elif choice == 'u':
            board.shift('up')

        elif choice == 'd':
            board.shift('down')

        elif choice == 'l':
            board.shift('left')

        elif choice == 'r':
            board.shift('right')

        else:
            print help_str


if __name__ == '__main__':
    new_game()
