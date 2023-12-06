import pyautogui
import os
import mouse
import sys 

import cProfile
import re

from time import sleep

#allows the import of local folders
sys.path.append('C:\Coding_Projects\Human-Benchmark-AimBot')
from utils.start import *


#returns if all the targets were clicked on (the save button has appeared)
# def isDone():

script_directory = os.path.dirname(os.path.abspath(__file__))

def main_controller():
    target_location = findTarget()
    count = 0
    while target_location != "not found":
        click_on(target_location.x, target_location.y)
        target_location = findTarget()
        

def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener(main_controller)

"""
This function takes advantage of the locateOnScreen function in pyautogui 
it finds where a certain picture is on the screen and returns x and y coords
"""
def findTarget(count=0):
    try:
        global script_directory
        image_path = os.path.join(script_directory, 'target.png')
        pyautogui.screenshot('debug_screenshot.png')
        target_location = pyautogui.locateCenterOnScreen(image_path, confidence=.5)
        return target_location

    except pyautogui.ImageNotFoundException:
        if(count >= 100):
            print("image could not be found")
            return "not found"
        findTarget(count=count+1)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "not found"

def click_on(horizontal_coor, vertical_coor):
    prevX, prevY = mouse.get_position()
    mouse.move(horizontal_coor, vertical_coor, absolute=True)
    mouse.click() 
    mouse.move(prevX, prevY)


if __name__ == "__main__":
    main()