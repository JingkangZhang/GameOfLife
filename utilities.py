# Game of life implemented in Python.
# Adapted from Stanford CS106B assignment.
# ReadyPython Sp19

import os
import random

def cls():
    '''Clears the terminal screen.'''
    os.system('cls' if os.name=='nt' else 'clear')

def print_welcome_message():
    '''Prints welcome messages to console.'''
    print("=============================================================")
    print("Welcome to ReadyPython Sp19 Game of Life!")
    print("Adapted from Stanford CS106B. Game of life is ")
    print("a simulation of the lifecycle of a bacteria colony.")
    print("Cells (X) live and die by the following rules:")
    print("- A cell with 1 or fewer neighbors dies.")
    print("- Locations with 2 neighbors remain stable.")
    print("- Locations with 3 neighbors will create life.")
    print("- A cell with 4 or more neighbors dies.\n")


def print_world(worldToPrint):
    '''Prints the formatted game world representations.'''
    for __ in __________: #FIXME
        for __ in ___________: #FIXME
            print(worldToPrint[i][j], end="")
        print()

def get_world():
    '''Asks the user for input and accordingly returns a 2D list representing the world.'''
    while True:
        fileName = input("Grid input file name? (or type 'random') ")
        if fileName == "random":
            return create_random_world()
        try:
            fhand = open("./worlds/" + fileName)
        except:
            print("Invalid file name. Try again.")
            continue
        return create_world(fhand)

def create_random_world():
    num_rows = random.randint(10, 30) #height range
    num_columns = random.randint(30, 70) #width range
    world = create_empty_2D_list(num_rows, num_columns)
    choices = ["-", "-", "-", "X"] #25% chance alive for each grid
    for i in range(num_rows):
        for j in range(num_columns):
            world[i][j] = random.choice(choices)
    return world


def create_world(fhand):
    curr_line = 0
    for line in fhand:
        curr_line += 1
        if(curr_line == 1):
            num_rows = _________ #FIXME
        elif(curr_line == 2):
            num_columns = _________ #FIXME
            world = create_empty_2D_list(num_rows, num_columns)
        elif(curr_line == num_rows + 3):
            break
        else:
            # FIXME: populate world with current line of input
    return world


def create_empty_2D_list(height, width):
    return [["" for column in range(width)] for line in range(height)]

def ask_wrap():
    while True:
        wrap = input("Should the simulation wrap around the grid (y/n)? ")
        _________ # FIXME: check if the input is correct and return


def ask_for_cmd():
    while True:
        cmd = input("t)ick, a)nimate, or q)uit? ")
        if cmd == 't' or cmd == 'a' or cmd == 'q':
            __________ # FIXME
        else:
            print("Please enter 't', or 'a', or 'q'" )
    return cmd

def ask_how_many_frames():
    while True:
        cmd = input("How many frames? ")
        try:
            cmd = int(cmd)
        except:
            print("Please enter an integer.")
            continue
        if cmd < 1:
            print("Please enter a positive integer.")
            continue
        return cmd


def calculate_next(world, wrap):
    newWorld = create_empty_2D_list(len(world), len(world[0]))
    for i in range(len(world)):
        for j in range(len(world[0])):
            neighbors = calculate_num_neighbors(world, i, j, wrap)
            if neighbors == 0 or neighbors == 1 or neighbors > 3:
                newWorld[i][j] = '-'
            elif neighbors == 3:
                newWorld[i][j] = 'X'
            elif neighbors == 2:
                newWorld[i][j] = world[i][j]
    return newWorld



def calculate_num_neighbors(world, i, j, wrap):
    sum = 0
    height = len(world)
    width = len(world[0])
    for row in range(i - 1, i + 2):
        for column in range(j - 1, j + 2):
            if wrap:
                row = (row + height) % height # modular trick for wrapping around grids. -1 => height - 1; height => 0
                column = (column + width) % width # similar to above
            else:
                #no wrapping. ignore out of range indices
                if row >= height or row < 0 or column >= width or column < 0:
                    continue
            if world[row][column] == "X":
                sum += 1
    if world[i][j] =="X":
        sum -= 1
    return sum
