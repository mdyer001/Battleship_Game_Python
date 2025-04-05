# Meagan Dyer 
# CS 5001 
# Main application for Battleship game 

import Board 
import random
import Ship
import Battleship

def main():
    print("Welcome to Battleship! Good Luck!")
    BattleshipGame = Battleship.Battleship()
    BattleshipGame.create_ships()
    BattleshipGame.place_comp_ships(BattleshipGame.comp_ships)
    BattleshipGame.UserOceanBoard.print_board()
    BattleshipGame.CompOceanBoard.print_board()
    BattleshipGame.place_user_ship(BattleshipGame.user_ships)
    allcompshipssunk = False
    allusershipssunk = False
    
    while allusershipssunk == False or allcompshipssunk == False:
        #turns taken by user and computer
        BattleshipGame.turn(True, BattleshipGame.comp_ships)
        if BattleshipGame.count_sunk_ships(BattleshipGame.comp_ships) == 5:
            allcompshipssunk = True
            print("You have won the game!")
            break
        if BattleshipGame.count_sunk_ships(BattleshipGame.user_ships) == 5:
            allusershipssunk = True
            print("You have lost the game")
            break
        BattleshipGame.turn(False, BattleshipGame.comp_ships)
        if BattleshipGame.count_sunk_ships(BattleshipGame.comp_ships) == 5:
            allcompshipssunk = True
            print("You have won the game!")
            break
        if BattleshipGame.count_sunk_ships(BattleshipGame.user_ships) == 5:
            allusershipssunk = True
            print("You have lost the game")
            break

if __name__ == "__main__":
    main()
    
