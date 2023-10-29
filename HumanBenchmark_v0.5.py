import mss
import keyboard
import threading
import os
import mouse

from screenshot import screenshot_area
from screenshot import take_screenshot
from screenshot import monitor
target_color = "#95c3e8"
start_button = "shift"

"""
this is where everything is actually put together/
where the main logic happens
"""
def main_controller():
    print("starting")
    find_target()

def click_on(horizontal_coor, vertical_coor):
    mouse.move(horizontal_coor, vertical_coor, absolute=True)
    mouse.click() 

def find_target():
    global monitor
    screenshot = take_screenshot()
    count = 0
    for vertical in range(monitor["top"], monitor["height"]-1):
        for horizontal in range(monitor["left"], monitor["width"]-1):
            # print(screenshot.pixel(horizontal,vertical))
            curr_pixel = screenshot.pixel(horizontal,vertical)
            (r,g,b) = curr_pixel
            if curr_pixel == (149,195,232):
                count += 1
                # print(curr_pixel)
                screenshot_area(horizontal, vertical)
                # print("clicking", horizontal,"  ", vertical)
                # click_on(horizontal, vertical)
    exit()





# initilizes the keyboard threads to begin and end the program
def begin_listener():
    keyboard.wait("shift")
    # queue the threads
    escape_thread = threading.Thread(target=escape_listener)
    main_thread = threading.Thread(target=main_controller)
    # Start all 
    escape_thread.start()
    main_thread.start()
def escape_listener():
    global running
    keyboard.wait("esc")
    running = False
    print("Emergency escape has been pressed, exiting now")
    exit()


#start of program
def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener()
    # find_target()

if __name__=="__main__":
    main()