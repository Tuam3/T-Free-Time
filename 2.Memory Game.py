import random # importing the random module to generate random values for the grids

# This program creates a memory game where the user has to find pairs of values in a grid.
# The game will have two grids, grid A and grid B, with random values.
# The values in each grid will be from two sets defined as set A and set B.
# These values will be displayed to the user as asterisks until they find a pair.
# The user will enter the coordinates of the values they want to match, and the program will check if they are a pair.
# If the values are a pair, they will be displayed to the user. Otherwise, the user will be informed that they are incorrect.
# The game will continue until all pairs are found, and the user will be congratulated.

# for the values, I chose QWERTYUIOP as set A and qwertyuiop as set B
# i chose it since as a kid, i used to play a game on where i had to match the uppercase letters to the lowercase letters
# and i thought it would be a fun idea to implement it in this assignemt rather than having random symbols or numbers. 

# the two sets of values to be used in the game
set_a = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
set_b = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']

# asking the user to enter the size of the grid
grid_size = input("Enter the size of the grid from 3 and 10: ")
while True:
    if grid_size.isdigit():
        grid_size = int(grid_size)
        if 3 <= grid_size <= 10:
            break
        else:
            grid_size = input("Please enter a valid number between 3 and 10: ")
    else:
        grid_size = input("Please enter an integer between 3 and 10: ")

# basically creating a dictionary to map the values of set a to set b
mapping = {set_a[i]: set_b[i] for i in range(len(set_a))}

# creating the two main grids with random values from set_a and set_b for grid_a and grid_b 

# grid_a with random values from set_a
grid_a = []    # empty list to store the values of grid a
for _ in range(grid_size):     # looping through and running grid_size times
    row = []       # empty list to store the values of the row
    for _ in range(grid_size):     # looping through the grid size
        row.append(random.choice(set_a))    # appending the random choice of set a to the row
    grid_a.append(row)   # appending the row to the grid a

# grid_b using the mapping from grid_a
grid_b = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        row.append(mapping[grid_a[i][j]])
    grid_b.append(row)

# making grid_b to shuffle its values, only shuffling grib b because a will already be random and shuffling b it will make it challenging  to find the pairs
shuff_grid_b = []      # empty list to store the values of grid b
for sublist in grid_b:        #l ooping through the grid b
    for item in sublist:        #l ooping through the sublist
        shuff_grid_b.append(item)        # appending the item to the empty list

random.shuffle(shuff_grid_b)

# reconstructing a new grid_b with shuffled values
grid_b = []
for i in range(grid_size):
    row = shuff_grid_b[i * grid_size:(i + 1) * grid_size]   
    grid_b.append(row)

# creating visibility grids to keep track of which values are visible to the user with False values using nested loops to create the 2D grid
# grid_a visibility
visible_a = []
for _ in range(grid_size):      # undetermined variable because we are not using it and runs grid_size times
    row = [] 
    for _ in range(grid_size): 
        row.append(False) 
    visible_a.append(row)    # this basically makes it so that the grid is not visible to the user until they find the pairs of the values

# grid_b visibility
visible_b = []
for _ in range(grid_size):
    row = []
    for _ in range(grid_size):
        row.append(False)
    visible_b.append(row)

                                    # creating the main loop to keep the game running, i call it the "Game code"
while True:
    # displaying grid_a
    for i in range(grid_size):     # looping through the grid size given by the user
        row_display = []
        for j in range(grid_size):    
            if visible_a[i][j]:
                row_display.append(grid_a[i][j])    # basically means that if the values of grid a are visible to the user, then they will be displayed
            else:
                row_display.append('*')   # if the values are not visible, then they will be displayed as an asterisk
        print(" ".join(row_display))
    
    print("------------------------")  # this is just to separate the two grids
    
    # displaying grid_b
    for i in range(grid_size):
        row_display = []
        for j in range(grid_size):
            if visible_b[i][j]:
                row_display.append(grid_b[i][j])
            else:
                row_display.append('*')
        print(" ".join(row_display))
    
    # getting the user's input to the coordinates of the grids. Starting with grid a and then grid b
    while True:
        x1, y1 = input("Enter coordinates for Grid A (row and column): ").split()   # splitting makes it so that the user can enter 2 values with a space between them
        x1, y1 = int(x1), int(y1)   # converting the values to integers
        x2, y2 = input("Enter coordinates for Grid B (row and column): ").split() 
        x2, y2 = int(x2), int(y2)
        
        if visible_a[x1][y1] or visible_b[x2][y2]:      # checking if the coordinates have already been matched and calling back to the empty variable visible_a and visible_b created earlier
            print("One or both of these coordinates have already been matched. Please choose different coordinates.")
        else:
            break

    # getting the the values of the coordinates to match
    if grid_b[x2][y2] == mapping[grid_a[x1][y1]]: # basically means if the values of grid b (x2, y2) are equal to the mapping of grid a (x1, y1) then the user has found a pair
        print("You got it, CORRECT!")
        visible_a[x1][y1] = True    # means that the values of grid a are now visible to the user
        visible_b[x2][y2] = True    # means that the values of grid b are now visible to the user
    else:
        print("Whoops, you are INCORRECT!")
        print(f"Grid A value: {grid_a[x1][y1]}") #printing the values of grid a and b to the user so they can see what they are matching
        print(f"Grid B value: {grid_b[x2][y2]}") 
    
    # finally, checking to see if all pairs are found and if so, the game ends
    all_pairs_found = True          #setting the variable to true so that the game can end if all pairs are found
    for row in visible_a:       # checking for all the rows in visible_a
        if not all(row):           # basically means that if all the values are NOT visible to the user, then the game will continue
            all_pairs_found = False         
            break
    if all_pairs_found:         #otherwise, if all the pairs are found, the game will end
        for row in visible_b:
            if not all(row):
                all_pairs_found = False
                break
    
    if all_pairs_found:        #printing a congratulatory message to the user if all pairs are found
        print("Congratulations! You've found all pairs!")
        break

    