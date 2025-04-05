#File which will hold the implementation of the Target Game board
# Created by Meagan Dyer 
#04/02/2023
import Ship as ship
import OceanBoard
import random as randint
import random


class TargetBoard:
    "Class TargetBoard" 
    "Attributes: location, rows, columns"
    "Methods: printboard(), PlaceHit(), PlaceMiss(), PlaceShip()"

    def __init__(self, name):
            self.name = name
            self.board = [[" "] * 8 for i in range(8)]
            self.key = {'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        
     
    # prints the board that will be a visual for the user. 
    def printboard(self):
        print(' A B C D E F G H')
        print(' ___________________')
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def get_ship_location(self):
            while True:
                try: 
                    row = input("Enter the row of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid letter between A-H')
            while True:
                try: 
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGH':
                        column = self.key(column)
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column
#computer create 5 ships
    def computer_create_ships(self):
        for i in range(5):
            ship_row, ship_column = random.randint(0,7), random.randint(0,7)
            while self.board[ship_row][ship_column] == "X":
                ship_row, ship_column = self.get_ship_location()
            self.board[ship_row][ship_column] = "X"

#user and computer turn
    def turn(self, board):
        if board == self.board:
            row, column = self.user_input()
            if self.board[row][column] == "-":
                self.turn(self.board)
            elif self.board[row][column] == "X":
                self.turn(self.board)
            elif self.board[row][column] == "X":
                self.board[row][column] = "X"
            else:
                self.board[row][column] = "-"
        else:
            row, column = random.randint(0,7), random.randint(0,7)
            if self.board[row][column] == "-":
                self.turn(self.board)
            elif self.board[row][column] == "X":
                self.turn(self.board)
            elif self.board[row][column] == "X":
                self.board[row][column] = "X"
            else:
                self.board[row][column] = "-"

    #player turn
            while True:
                print('Guess a battleship location')
                TargetBoard.printboard()
                TargetBoard.turn(self.board)
                return self.board
        if self.count_hit_ships(self.board) == 17:
                    print("You win!")
                    return self.board  
    #computer turn
        while True:
                self.turn(self.board)
                return self.board          
                print_board()   
        if self.count_hit_ships(self.board) == 17:
            print("Sorry, the computer won.")
            return self.board

    
