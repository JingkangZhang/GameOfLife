# Game of life implemented in Python.
# Adapted from Stanford CS106B assignment.
# ReadyPython Sp19

from utilities import *
from time import sleep

print_welcome_message()
world = get_world()
wrap = ask_wrap() #Boolean
print_world(world)

while True:
    cmd = ask_for_cmd() #"t", "a", or "q"
    if cmd == "t": # tick once, printing the resulting state after 1 step.
        world = calculate_next(world, wrap)
        print_world(world)
    elif cmd == "a": # animate
        frames = ask_how_many_frames()
        while frames > 0:
            cls()  #clears the screen
            world = calculate_next(world, wrap)
            print_world(world)
            sleep(.15)
            frames -= 1
    elif cmd == "q": # quit
        break
print("Have a nice life.")
