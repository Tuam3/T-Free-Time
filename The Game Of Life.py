#Underpopulation: A living cell with fewer than two living neighbors dies (as if by loneliness)
#Stable Population: A living cell with two or three living neighbors survives to the next generation
#Overpopulation: A living cell with more than three living neighbors dies (as if by overcrowding)
#Reproduction: A dead cell with exactly three living neighbors becomes a living cell (as if by reproduction)

#The Grid: The game is played on a grid (in our case, 6x6). Each cell in the grid can be either alive (represented by a '1') or dead (represented by a '0')
#Neighbors: Each cell has eight neighbors: the cells directly above, below, to the left, to the right, and the four diagonal neighbors
#Generations: The game proceeds in discrete steps called "generations" or "rounds." 
#In each generation, every cell's state is updated simultaneously based on the rules and the state of its neighbors in the previous generation.
#Initial State (Seed): The game begins with an initial configuration of living cells (the "seed"). This seed is provided by the user

print("""Welcome to the Game of Life!

In this game, you will provide the initial configuration of living cells (the 'seed') and watch them evolve over generations based on the following rules:

The Grid: The game is played on a grid (in our case, 6x6). Each cell can be either alive ('1') or dead ('0').
Neighbors: Each cell has eight neighbors (above, below, left, right, and diagonals).
Generations: The game proceeds in 'generations.'  Each cell's state is updated based on its neighbors.
Initial State (Seed): The game begins with a user-provided 'seed' of living cells.

Rules of the Game:

Evolution: Cells live, die, or are born based on their neighbor count.
Underpopulation: A living cell with < 2 living neighbors dies.
Stable Population: A living cell with 2 or 3 living neighbors survives.
Overpopulation: A living cell with > 3 living neighbors dies.
Reproduction: A dead cell with exactly 3 living neighbors becomes alive.

""")

# This process continues until the user quits the program

#firstyl creating a 6x6 grid based on the seed coordinates.
def get_initial_grid(rows, cols, seed):
    grid= [[0 for _ in range(cols)] for _ in range(rows)]  #sets grid with all cells to 0 (dead)

    for x, y in seed:  #iterating over the seed coordinates
        if 0 <=x < rows and 0 <=y <cols:  #if the seed coordinates are within the grid bounds
            grid[x][y] =1  #then set the cell to 1 (live) if the coordinates are valid
    return grid  

#counting the live neighbors of a cell
def count_live_neighbors(grid, x, y):
    rows, cols= len(grid), len(grid[0])  #gettin the number of rows and columns in the grid
    count =0 

    for i in range(-1, 2):  #goinng over the neighboring rows(i) and column(j)
        for j in range(-1, 2): 
            if i==0 and j==0:  #skipping the cell itself
                continue
            nx, ny =x + i, y +j  #calculating the neighbor's coordinates. nx and ny are the neighboring cell's coordinates.
            if 0 <= nx < rows and 0 <=ny <cols and grid[nx][ny] ==1:  #if the neighbor is within bounds and alive, increment the count
                count +=1 
    return count  

#the next generation of the grid or the updated grid
def update_grid(grid):
    rows, cols =len(grid), len(grid[0])  
    new_grid =[[0 for _ in range(cols)] for _ in range(rows)]  #as explained previously

    for x in range(rows):  
        for y in range(cols):  
            live_neighbors =count_live_neighbors(grid, x, y)  #counting the live neighbors of the current cell
            if grid[x][y] ==1:  #if the current cell is alive 
                if live_neighbors < 2 or live_neighbors > 3:  # if the cell is 0 or more than 3, it dies in the next generation. (underpopulation or overpopulation)
                    new_grid[x][y] =0  
                elif 2 <= live_neighbors <= 3:  #f it has 2 or 3 live neighbors the cell stays alive. (stable population)
                    new_grid[x][y] =1  
            else:  # If the current cell is dead.
                if live_neighbors ==3:  #if the cell has exactly 3 live neighbors, it becomes alive in the next generation. (reproduction)
                    new_grid[x][y] =1  
    return new_grid  

#Prints the grid
def display_grid(grid):
    for row in grid:  
        print("".join(map(str, row)))  #row as a string of 0s and 1s

#seed coordinates from the user
def get_seed_coordinates():
    seed =[]  # empty list to store seed coordinates

    while True:  # a while loop to get user input until 'done' is entered
        coord_str =input("Enter coordinates for a live cell (x, y), or type 'done': ") 
        if coord_str.lower() =='done': 
            break #exits the loop if the user enters 'done'

        x, y =map(int, coord_str.strip("()").split(","))  #splitting the input string and converting the coordinates to integers
        if 0 <=x <6 and 0 <=y <6:  #validating the coordinates
            seed.append((x, y))  #adding it back to the to the empty seed list
        else:
            print("Invalid coordinates. Row and column must be between 0 and 5.") 
    return seed  #return it  the list of seed 


seed =get_seed_coordinates()  # Get the seed coordinates from the user
grid =get_initial_grid(6, 6, seed)  # Create the initial grid with the seed coordinates.
display_grid(grid)  # Display the initial grid.

#the main loop
while True:  
    user_input =input("Press Enter for next round, 'q' to quit: ")  
    if user_input.lower() =='q':  
        break  # Exit the loop if the user wants to quit

    grid =update_grid(grid)  #update the grid to the next generation
    display_grid(grid)  #display the updated grid
