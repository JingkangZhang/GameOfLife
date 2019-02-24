# Game of life implemented in Python.
# Adapted from Stanford CS106B assignment.
# ReadyPython Sp19

# Feel free to delete anything and implement it your own way!
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
    '*** YOUR CODE HERE ***'

def get_world():
    '''Asks the user for input and accordingly returns a 2D list representing the world.'''
    '*** YOUR CODE HERE ***'

def create_random_world():
    '*** YOUR CODE HERE ***'

def create_world(fhand): #reading from files to be covered in Lecture 6. Learning it yourself on py4e totally manageable.
    '*** YOUR CODE HERE ***'

def create_empty_2D_list(height, width):
    '*** YOUR CODE HERE ***'

def ask_wrap():
    '*** YOUR CODE HERE ***'

def ask_for_cmd():
    '*** YOUR CODE HERE ***'

def ask_how_many_frames():
    '*** YOUR CODE HERE ***'

def calculate_next(world, wrap):
    '*** YOUR CODE HERE ***'

def calculate_num_neighbors(world, i, j, wrap):
    '*** YOUR CODE HERE ***'
