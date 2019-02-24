from utilities import *
from time import sleep

print_welcome_message()
world = get_world()
wrap = ask_wrap()
print_world(world)

while True:
    cmd = ask_for_cmd()
    if cmd == "t":
        world = calculate_next(world, wrap)
        print_world(world)
    elif cmd == "a":
        frames = ask_how_many_frames()
        while frames > 0:
            cls()  #clears the screen
            world = calculate_next(world, wrap)
            print_world(world)
            sleep(.15)
            frames -= 1
    elif cmd == "q":
        break
print("Have a nice life.")
