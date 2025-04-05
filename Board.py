# Meagan Dyer 
# CS5001 
# Class to create the board in Battleship

import random
import Ship

class Board:
    def __init__(self):
        self.board = [[" "] * 8 for i in range(8)]


    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1