import mss
import keyboard
import threading
import os
import mouse

from screenshot import screenshot_area
from screenshot import take_screenshot
from screenshot import monitor

target_color = (149, 195, 232)
start_button = "shift"
running = True
"""
this is where everything is actually put together/
where the main logic happens
"""
def main_controller():    
    global running
    screenshot = take_screenshot()
    save_color = (255,209,84)
    while screenshot.pixel(450,450) != save_color:
        screenshot = take_screenshot()
        find_target(screenshot)
    else:
        print("ending game...")
        running = False

        


def click_on(horizontal_coor, vertical_coor):
    mouse.move(horizontal_coor, vertical_coor, absolute=True)
    mouse.click() 

def find_target(screenshot):
    global monitor, running
    if running == False:
        return
    for vertical in range(0, screenshot.height):
        for horizontal in range(0, screenshot.width):
            #these are the coords on the actual screen
            x = horizontal + monitor["left"]
            y = vertical + monitor["top"]

            curr_pixel = screenshot.pixel(horizontal,vertical)
            #clicks on targets pixels
            if curr_pixel == (149,195,232):
                click_on(x, y)
                return



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
    while not running:
        keyboard.wait("esc")
        running = False
    exit()


#start of program
def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener()
    # find_target()

if __name__=="__main__":
    main()