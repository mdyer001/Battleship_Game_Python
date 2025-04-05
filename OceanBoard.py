#File which will hold the implementation of the Ocean Game board
# Created by Meagan Dyer 
#04/02/2023
import Ship as ship
import random as randint
import random

class OceanBoard:
    "Class OceanBoard" 
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
        row_number = 1
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
                    column = self.key[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column
    
    # def create_ships(self):
    #     for i in range(5):
    #         self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
    #     while self.board[self.x_row][self.y_column] == "X":
    #         self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
    #         self.board[self.x_row][self.y_column] = "X"
    #     return self.board

    # def get_user_input(self):
    #     try:
    #         x_row = input("Enter the row of the ship: ")
    #         while x_row not in '12345678':
    #             print('Not an appropriate choice, please select a valid row')
    #             x_row = input("Enter the row of the ship: ")

    #         y_column = input("Enter the column letter of the ship: ").upper()
    #         while y_column not in "ABCDEFGH":
    #             print('Not an appropriate choice, please select a valid column')
    #             y_column = input("Enter the column letter of the ship: ").upper()
    #             return int(x_row) - 1, self.key[y_column]
    #     except ValueError and KeyError:
    #         print("Not a valid input")
    #     return self.get_user_input()
#computer create 5 ships
    def computer_create_ships(self):
        for i in range(5):
            (ship_row, ship_column) = random.randint(0,7), random.randint(0,7)
            while (self.board[ship_row][ship_column]) == "X":
                (ship_row, ship_column) = self.get_ship_location()
                self.board[ship_row][ship_column] = "X"


#player creates 5 ships
    def player_create_ships(self):
        for i in range(5):
            self.printboard()
            (ship_row, ship_column) = self.get_ship_location()
            while self.board[ship_row][ship_column] == "X":
                print("That location is already taken, choose another")
                (ship_row, ship_column) = OceanBoard.get_ship_location()
            self.board[ship_row][ship_column] = "X"

    # check if ship fits in board
    def check_ship_fit(self, ship_length, row, column, orientation):
        if orientation == "H":
            if column + ship_length > 8:
                return False
            else:
                return True
        else:
            if row + ship_length > 8:
                return False
            else:
                return True
        
 # Checks to see if the ships that are being placed will overlap       
    def ship_overlaps(self, row, column, orientation, ship):
        if orientation == "H":
            for i in range(column, column + ship.location):
                if self.board[row][i] == "X":
                    return True
        else:
            for i in range(row, row + ship.length):
                if self.board[i][column] == "X":
                    return True
        return False

    def user_input(self, place_ship):
        if place_ship == True:
            while True:
                try: 
                    orientation = input("Enter orientation (H or V): ").upper()
                    if orientation == "H" or orientation == "V":
                        break
                except TypeError:
                    print('Enter a valid orientation H or V')
            while True:
                try: 
                    row = input("Enter the row 1-8 of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid letter between 1-8')
            while True:
                try: 
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGH':
                        column = self.key[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column, orientation 
        else:
            while True:
                    try: 
                        row = input("Enter the row 1-8 of the ship: ")
                        if row in '12345678':
                            row = int(row) - 1
                            break
                    except ValueError:
                        print('Enter a valid letter between 1-8')
            while True:
                    try: 
                        column = input("Enter the column of the ship: ").upper()
                        if column in 'ABCDEFGH':
                            column = self.key[column]
                            break
                    except KeyError:
                        print('Enter a valid letter between A-H')
            return row, column  

        

# places the ships on a location on the board where they will fit. 
    def PlaceShip(self, ship):
        #loop through length of ships
            for ship_length in ship.length:
        #loop that until ship fits continues to run esuring the ship doesn't overlap
                while True:
                    if self.board == self.name:
                        orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                        if self.check_ship_fit(self, row, column, orientation):
        
                    #checks to see if ship overlaps
                            if self.ship_overlaps(self, row, column, orientation, ship_length) == False:
                        #places ships
                                if orientation == "H":
                                    for i in range(column, column + ship_length):
                                        self.board[row][i] = "X"
                                else:
                                    for i in range(row, row + ship_length):
                                        self.board[i][column] = "X"
            else:
                    place_ship = True
                    print('Place the ship with a length of ' + str(ship_length))
                    row, column, orientation = self.user_input(place_ship)
                    if self.check_ship_fit(ship_length, row, column, orientation):
                        #check if ship overlaps
                            if self.ship_overlaps(self, row, column, orientation, ship_length) == False:
                                #place ship
                                if orientation == "H":
                                    for i in range(column, column + ship_length):
                                        self.board[row][i] = "X"
                                else:
                                    for i in range(row, row + ship_length):
                                        self.board[i][column] = "X"
                                        self.printboard

#check if all ships are hit
    def count_hit_ships(self):
        count = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    count += 1
        return count



testboard = OceanBoard("testboard")
testboard.printboard()
# testboard.user_input(ship.Ship) #Not really important, just takes in input, why cant this be in the actual function? 
testboard.computer_create_ships()
# testboard.player_create_ships()
# testboard.get_ship_location()
# testboard.PlaceShip()



