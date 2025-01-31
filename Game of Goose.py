#Description: A simple game of goose where two players take turns to roll a dice and move their pieces on the board. 
# Three special tiles are present on the board: bridges, hotels, and the winning tile.
# If a player lands on a bridge, they move to the other end of the bridge. If they land on a hotel, they skip their next turn.
# The game board moves from 1 to 64 in a snake-like spiral pattern with 8 rows and 8 columns 
# The game board is displayed at the start of the game and after each turn to show the positions of the players.
# The game marks the positions of the players with P1 and P2, and the special tiles with B1, B2 for the bridges, H1, and H2 for the hotels.
# Each player takes turns to roll a dice and move their piece on the board. 
# Player 1 is blue and Player 2 is red.
# The game ends when a player reaches the winning tile (64) and the winner is declared.

import random #for the dice roll 

#defining the game board
board =[[15, 16, 17, 18, 19, 20, 21, 22], 
        [14, 39, 40, 41, 42, 43, 44, 23], 
        [13, 38, 55, 56, 57, 58, 45, 24], 
        [12, 37, 54, 63, 64, 59, 46, 25], 
        [11, 36, 53, 62, 61, 60, 47, 26], 
        [10, 35, 52, 51, 50, 49, 48, 27], 
        [9, 34, 33, 32, 31, 30, 29, 28], 
        [8, 7, 6, 5, 4, 3, 2, 1]] 

#defining the special tiles on the board
bridges ={6: "B1", 21: "B1", 41: "B2", 56: "B2"}
hotels ={11: "H1", 26: "H2", 36: "H1", 60: "H2"}

#to print the game board with the special tiles and player positions
def print_board(board, bridges, hotels, player1_pos=0, player2_pos=0):
    rows =len(board)  # Number of rows in the board
    cols =len(board[0])  # Number of columns in the board 

    for row in range(rows):  # Loop through each row
        print("|", end="")  # Print the left border of the row
        for col in range(cols):  # Loop through each column
            number =board[row][col]  # Get the board number at the current position
            if number ==player1_pos and number == player2_pos:
                print("\033[34m P1\033[0m\033[31mP2 \033[0m|", end="")  # Blue P1 and Red P2
            elif number ==player1_pos:
                print("\033[34m P1  \033[0m|", end="")  # Blue P1 \033[34m is an ANSI escape code that changes the text color to blue
            elif number ==player2_pos:
                print("\033[31m P2  \033[0m|", end="")  # Red P2 \033[31m is an ANSI escape code for red.
            elif number in bridges:
                print(f" {bridges[number]:^4} |", end="")  #addin the bridge tile
            elif number in hotels:
                print(f" {hotels[number]:^4} |", end="")  #addin the hotel tile
            else:
                print(f" {number:^4} |", end="")  #printing a  regular tile
        print()  
        print("-" * (cols * 7 + 1))  #a horizontal line to separate the rows
    print()  

#displaying the game board at teh start of the game
print_board(board, bridges, hotels)

#the dice roll function to generate a random number between 1 and 6 
def roll_dice():
    return random.randint(1, 6) 

#moving the players based on the dice roll
def move_player(position, roll):
    new_position = position +roll  #movin the player by the dice roll
    if new_position >64:
        new_position =64 - (new_position -64)  #bouncing back as per the requirement if over 64
    return new_position  #return to the new position

#if the player lands on a special tile
def check_special_tiles(position, bridges, hotels, skip_turn):
    if position in bridges:
        if position ==6:
            position =21  #moving the players to bridge 21 if they land on bridge 6
        elif position ==41:
            position =56  #moving the players to bridge 56 if they land on bridge 41
    if position in hotels:
        skip_turn =True  #skips next turn if landing on a hotel
    return position,skip_turn  

#to display the game board with player positions each turn
def display_board(board, bridges, hotels, player1_pos, player2_pos):
    print_board(board, bridges, hotels, player1_pos, player2_pos) #displaying the board with player positions


                                                                                #the main game function
def game():
    player1_pos =1  #players starting at position 1
    player2_pos =1  
    player1_skip =False  #makin it so that skip flag for Player 1 set to False means no skip
    player2_skip =False  
    turn =1  #setting a turn counter as player 1 goes first (turn 1)

    while player1_pos !=64 and player2_pos !=64: #continues until a player reaches the winning position (64)
        # Determine the current player's turn (Player 1 on odd turns, Player 2 on even)

        if turn % 2 != 0:  # Player 1's turn
            print(f"Turn {turn}: Player 1") #Added to display current turn and player for better readability.
            if not player1_skip:  #if Player 1 needs to skip a turn (due to landing on a hotel) using ifnot since hotels arent that common on the board and has less chance of landing on it.
                input("Player 1, press Enter to roll the dice...")
                roll =roll_dice()  #calling back the dice roll function to roll the dice 
                print(f"You rolled a {roll}") 
                player1_pos =move_player(player1_pos, roll)  #this will update player 1's position on the board
                player1_pos, player1_skip =check_special_tiles(player1_pos, bridges, hotels, player1_skip)#checks for bridges and hotels after the move and return the updated position/flags.
            else: #if player 1 needs to skip a turn due to the hotel
                print("Player 1 skips this turn due to the hotel.") 
                player1_skip =False  #resets the skip flag so Player 1 can play on their next turn

        else:  # Player 2's turn (similar to Player 1's turn's code)
            print(f"Turn {turn}: Player 2")
            if not player2_skip:  
                input("Player 2, press Enter to roll the dice...")
                roll =roll_dice()  
                print(f"You rolled a {roll}")  
                player2_pos =move_player(player2_pos, roll)  
                player2_pos, player2_skip =check_special_tiles(player2_pos, bridges, hotels, player2_skip)
            else:
                print("Player 2 skips this turn due to the hotel.")  
                player2_skip = False  

        display_board(board, bridges, hotels, player1_pos, player2_pos) #displaying the board to show current player positions each turn.
        turn +=1  #incrementing the turn counter to switch to the next player

    #after the game loop ends when a player reaches 64
    if player1_pos ==64: 
        print("Congratulations!!!\nPlayer 1 wins!") 
    else:
        print("Congratulations!!!\nPlayer 2 wins!") 

game() 
