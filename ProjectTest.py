# Meagan Dyer 
# Test file for the classes of the Battleship game 

import random
import Battleship
import Ship
import Board 

def main():               
    #Create Battlehship Object
    test = Battleship()

    #testing that ships are being created and stored within the lists
    test.create_ships()
    print(test.user_ships)
    print(test.comp_ships)


    #Testing if check_ship_fit works, based off of different parameters
    print(test.check_ship_fit(test.user_ships[0],7,7,"H"))
    print(test.check_ship_fit(test.user_ships[0],1,1,"H"))

    #Checking if ship_overlap works by placing a fake ship on the board. 
    test.UserOceanBoard.board[0][0] = "*"
    print(test.ship_overlaps(test.UserOceanBoard.board, 0, 0, "H", test.comp_ships[0]))
    print(test.ship_overlaps(test.UserOceanBoard.board, 5, 5, "H", test.comp_ships[4]))
    test.UserOceanBoard.print_board()

    # Checking to see if user_input works by specifying if placeship is True or not 
    print(test.user_input(True))
    # The numbers that come out are correct it is showing the information that the board 
    # receives in order to place ships and access misses

    # Checks to see if place_comp_ships works by checking if the ships get placed correctly on the board 
    (test.place_comp_ships(test.comp_ships))
    test.CompOceanBoard.print_board()
    for ship in test.comp_ships:
        print(ship.location)

    # Checks to see if place_user_ships works by checking if the ships get placed correctly on the board 
    # (test.place_user_ship(test.user_ships))
    # test.UserOceanBoard.print_board()

    # # Checks to see if count_hit_ships works by using the HitIncrease method in the Ship class and calling on count_hit_ships
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))
    # test.comp_ships[0].HitIncrease()
    # print(test.count_sunk_ships(test.comp_ships))


    # Checks the turn method by calling on a user turn and entering a possible hit and miss 
    test.turn(True, test.user_ships)

if __name__ == "__main__":
    main()