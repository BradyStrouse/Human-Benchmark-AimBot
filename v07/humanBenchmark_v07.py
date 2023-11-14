import mss
import keyboard
import threading
import os
import mouse

import sys 

from time import sleep

from utils.screenshot import screenshot_area, take_screenshot
from utils.screenshot import take_screenshot
from utils.screenshot import monitor

from utils.start import *


"""
In v0.7 I took v0.5 and optomized it, there are no significant changes, just small things
"""


target_color = (149, 195, 232)
start_button = "shift"
running = True


"""
this is where everything is actually put together/
where the main logic happens
"""
#delete later
global screenshot
def main_controller():    
    global running, screenshot
    print("starting...")

    #clicks on the inital target
    click_on(910,450)

    screenshot = take_screenshot()
    # this is the color of the save button
    save_color = (255,209,84)
    while screenshot.pixel(450,450) != save_color and running == True:
        screenshot = take_screenshot()
        find_target(screenshot)
        sleep(.008)
    else:
        print("ending game...")
        try:
            keyboard.unhook_all()
        except Exception as e:
            print(f"Error unhooking keyboard: {e}")
        running = False
        sys.exit()

        


def click_on(horizontal_coor, vertical_coor):
    mouse.move(horizontal_coor, vertical_coor, absolute=True)
    mouse.click() 

def find_target(screenshot):
    global monitor, running
    if running == False:
        return
    for vertical in range(0, screenshot.height, 70):
        for horizontal in range(0, screenshot.width, 50):
            #these are the coords on the actual screen
            x = horizontal + monitor["left"]
            y = vertical + monitor["top"]

            curr_pixel = screenshot.pixel(horizontal,vertical)
            (r,g,b) = curr_pixel
            #clicks on targets pixels
            if curr_pixel == (149,195,232) or curr_pixel == (255,255,255):
                click_on(x, y)
                return
            
def set_running(run):
    global running
    running = run
    if running == False:
        exit()
    
#start of program
def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener(main_controller)
    # find_target()

if __name__=="__main__":
    main()