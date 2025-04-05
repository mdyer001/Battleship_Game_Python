#File which will hold the implementation of the Game rules
# Created by Meagan Dyer 
#04/02/2023
import random
import Ship
import Battleship
import Cruiser
import Submarine
import Destroyer
import OceanBoard


class Game:
    "Class Game" 
    "Attributes: rules,board, ship, location"
    "Methods: ShipInput(), CreateBoards(), guess(), HitorMiss(), SunkShip(), count_hit_ships(), runGame()"

    def __init__(self, location, player_board,opponent_board, ship):
        self.location = location
       #Boards include: Opponent Ocean, Player Ocean, Opponent Target
       # Player Target 
        self.board = player_board, opponent_board
        self.ship = ship

    def ShipInput(Opponent_ocean,Player_ocean):
        player_ships = input(int("place your 5 ships on your Ocean Board"))
        Player_ocean = player_ships
        opponent_ships = random.randint()
        Opponent_ocean = opponent_ships

    def CreateBoards(opponent_board, player_board):
        Opponent_ocean = opponent_board
        Opponent_target = opponent_board
        Player_ocean = player_board
        Player_target = player_board

    def guess(opponent_guess, player_guess, guess):
        opponent_guess = guess
        player_guess = guess 
        let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        player_guess = row=input('Please enter a ship row 1-8').upper()
        while row not in '12345678':
            print("Please enter a valid row")
            row=input('Please enter a ship row 1-8')
        #Enter the Ship column from A TO H
        player_guess = column=input('Please enter a ship column A-H').upper()
        while column not in 'ABCDEFGH':
            print("Please enter a valid column")
            column=input('Please enter a ship column A-H')
            return int(row)-1,let_to_num[column]
        opponent_guess = random.randint(row)
        opponent_guess = random.randint(column)

    def HitorMiss(ship_location,row,column,ship, player_guess, opponent_guess):
        [row][column] = ship_location
        if player_guess == ship_location[row][column] =='X':
            print(' Congratulations you have hit the...'+ ship)
            Player_target = "X"
        elif opponent_guess == ship_location[row][column] =='X':
            print(' Congratulations the opponent has hit the...'+ ship)
            Opponent_target = "X"
        else:
            print('Sorry,You missed')
            Player_target = '-'
            Opponent_target = '-'
    
    def SunkShip(ship_location, ship_length, ship):
        if ship_location == "X":
            ship_length = "X"
            print("congrats you sunk the" + ship)

    def count_hit_ships(board):
        count=0
        for row in board:
            for column in row:
                if column=='X':
                    count+=1
        return count
    
    def runGame(self, player_ocean, player_target, location):
        print('Welcome to Battleship')
        print(player_ocean)
        row,column = location
        if player_target[row][column] == '-':
            print(' You already guessed that') 
        else:
            self.HitorMiss(location)
        if  self.count_hit_ships(player_target) == 5:
                print("Congratulations you have sunk all the battleships")
    















