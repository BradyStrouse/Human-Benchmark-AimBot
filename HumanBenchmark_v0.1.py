import mouse
import threading
import keyboard
# v0.1 is a use of just clicking is every spot that the hitbox could be
# to be able to confirm a hit on every possible circle in a line, you need to touch every 70 pixels
# The playable feild is 785 wide and 440 long (approximate)

#goes through all possible spots and clicks on them

#tells if the program should be running to other threads
running = True

def goThrough():
    global running 
    max_score = 30
    # Define the boundaries of the zone
    left_x, right_x = 515, 1500
    top_y, bottom_y = 200, 650

    # Define the width and height of the 70-pixel box
    box_width, box_height = 70, 70

    # Calculate the number of rows and columns
    num_rows = (bottom_y - top_y) // box_height
    num_cols = (right_x - left_x) // box_width
    # Do it 30 times to get them all
    for i in range(max_score):
        # Iterate through all possible positions within the zone
        for row in range(num_rows):
            for col in range(num_cols):
                # Calculate the center of each box and click 
                if(running):
                    box_center_x = left_x + col * box_width + box_width // 2
                    box_center_y = top_y + row * box_height + box_height // 2
                    mouse.move(box_center_x, box_center_y, absolute=True, duration=0.0009 )
                    mouse.click() 
                else: return


def start_listener():
    keyboard.wait("shift")
    print('starting')
    # Create a background threads for emergency escape and the actual clicking
    escape_thread = threading.Thread(target=escape_listener)
    clicker = threading.Thread(target=goThrough)
    # Start all 
    escape_thread.start()
    clicker.start()
def escape_listener():
    global running
    keyboard.wait("esc")
    running = False
    print("Emergency escape has been pressed, exiting now")
    exit()

if __name__ == '__main__':
    start_thread = threading.Thread(target=start_listener)
    start_thread.start()
    