#Meagan Dyer 
# CS5001 
# Class to create the rules of the game Battleship 

import random
import Ship
import Board

class Battleship:
    
    def __init__(self):
        '''Constructor for battleship class
        Creates all of the boards for the game:
        UserOceanBoard - Where the user will place thier ships
        CompOceanBoard - Where the computer will place thier ships
        UserTargetBoard - Where the users guesses will be stored, which will also
            be printed as the game is being played
        CompTargetBoard - Where the computers guesses will be stored'''
        self.UserOceanBoard = Board.Board()
        self.CompOceanBoard = Board.Board()
        self.UserTargetBoard = Board.Board()
        self.CompTargetBoard = Board.Board()
        self.key = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.user_ships = []
        self.comp_ships = []
        pass

    def create_ships(self):
        '''Creates all 5 ships for the game, using the Ship class. Will be able to
        create ships.
        Will return two lists containing all of the ships, one 
        for the user, one for the computer.'''

        # creates the list of User ships 
        UserCarrier = Ship.Ship("Carrier", 5)
        self.user_ships.append(UserCarrier)
        UserBattleship = Ship.Ship("Battleship", 4)
        self.user_ships.append(UserBattleship)
        UserCruiser = Ship.Ship("Cruiser", 3)
        self.user_ships.append(UserCruiser)
        UserSubmarine = Ship.Ship("Submarine", 3)
        self.user_ships.append(UserSubmarine)
        UserDestroyer = Ship.Ship("Destroyer", 2)
        self.user_ships.append(UserDestroyer)
        
        # creates the list of computer ships
        CompCarrier = Ship.Ship("Carrier", 5)
        self.comp_ships.append(CompCarrier)
        CompBattleship = Ship.Ship("Battleship", 4)
        self.comp_ships.append(CompBattleship)
        CompCruiser = Ship.Ship("Cruiser", 3)
        self.comp_ships.append(CompCruiser)
        CompSubmarine = Ship.Ship("Submarine", 3)
        self.comp_ships.append(CompSubmarine)
        CompDestroyer = Ship.Ship("Destroyer", 2)
        self.comp_ships.append(CompDestroyer)

    

    def check_ship_fit(self, ship, row, column, orientation):
        '''Checks if the ship fits on the board, given the ship length, 
        the row it is being placed, the column it is being placed, and the 
        orientation it is being placed'''
        if orientation == "H":
            if column + ship.length > 8:
                return False
            else:
                return True
        else:
            if row + ship.length > 8:
                return False
            else:
                return True
            
    
    def ship_overlaps(self, board, row, column, orientation, ship):
        '''checks to see each position for overlap '''
        if orientation == "H":
            for i in range(column, column + ship.length):
                if board[row][i] == "*":
                    return True
        else:
            for i in range(row, row + ship.length):
                if board[i][column] == "*":
                    return True
        return False

    
    def user_input(self, placeship):
        '''Takes in the user inputs to place ships if placeship is True,
        otherwise it used for input when the game is executing'''
        if placeship == True:
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
                    row = input("Enter a row 1-8 for where you want to shoot: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid letter between 1-8')
            while True:
                try: 
                    column = input("Enter a column for where you want to shoot: ").upper()
                    if column in 'ABCDEFGH':
                        column = self.key[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column 

    def place_comp_ships(self, ship_list):
        '''Places all 5 of the computer's ships on the computer ocean board'''
        for ship in ship_list:
            #loop until ship fits and doesn't overlap
            while True:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if self.check_ship_fit(ship, row, column, orientation):
                    #check if ship overlaps
                    if self.ship_overlaps(self.CompOceanBoard.board, row, column, orientation, ship) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship.length):
                                self.CompOceanBoard.board[row][i] = "*"
                                ship.location.append((row, i))
                        else:
                            for i in range(row, row + ship.length):
                                self.CompOceanBoard.board[i][column] = "*"
                                ship.location.append((i, column))
                        break
    
    def place_user_ship(self, ship_list):
        '''Places all 5 of the user's ships based on user input, and will print
        out a view of the location of all the ships'''

        for ship in ship_list:
            while True:
                row, column, orientation = self.user_input(True)
                if self.check_ship_fit(ship, row, column, orientation):
                    #check if ship overlaps
                        if self.ship_overlaps(self.UserOceanBoard.board, row, column, orientation, ship) == False:
                            #place ship
                            if orientation == "H":
                                for i in range(column, column + ship.length):
                                    self.UserOceanBoard.board[row][i] = "*"
                                    ship.location.append((row, i))
                            else:
                                for i in range(row, row + ship.length):
                                    self.UserOceanBoard.board[i][column] = "*"
                                    ship.location.append((i, column))
                            self.UserOceanBoard.print_board()
                            break 

        

    def count_sunk_ships(self, ship_list):
        '''returns the number of ships sunk, based off of 
        the ship_list'''
        count = 0 

        for ship in ship_list:
            if ship.sunk == True:
                count = count + 1
        return count
    
    def turn(self, user, ship_list):
        '''executes a turn for either the computer or the user.
        hits and misses will be stored in corresponding boards, and hits will 
        be stored within ship lists'''
        if user == True:
            row, column = self.user_input(False)
            if self.UserTargetBoard.board[row][column] == "-" or self.UserTargetBoard.board[row][column] == "X":
                print("you guessed that one already")
                self.UserTargetBoard.print_board()
                self.turn(user, ship_list)
            elif self.CompOceanBoard.board[row][column] == "*":
                print("hit")
                self.UserTargetBoard.board[row][column] = "X"
                for ship in ship_list:
                    for coord in ship.location:
                        if coord[0] == row and coord[1] == column:
                            ship.HitIncrease()
                self.UserTargetBoard.print_board()
                if self.count_sunk_ships(ship_list) != 5:
                    self.turn(user, ship_list)

            else:
                print("miss")
                self.UserTargetBoard.board[row][column] = "-"
                self.UserTargetBoard.print_board()

            
        else:
            row, column = random.randint(0,7), random.randint(0,7)
            if self.CompTargetBoard.board[row][column] == "-" or self.CompTargetBoard.board[row][column] == "X":
                self.turn(user, ship_list)
            elif self.UserOceanBoard.board[row][column] == "*":
                print("the computer hit")
                self.CompTargetBoard.board[row][column] = "X"
                for ship in ship_list:
                    for coord in ship.location:
                        if coord == (row,column):
                            ship.HitIncrease()
                self.turn(user, ship_list)
            else:
                print("the computer missed")
                self.CompTargetBoard.board[row][column] = "-"
def main():               

    if __name__ == "__main__":

        main()