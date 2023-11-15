import pyautogui
import os
import mouse
import sys 

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
    print(target_location)
    while target_location != "not found":
        click_on(target_location.x, target_location.y)
        target_location = findTarget()
        print(target_location)


"""
This function takes advantage of the locateOnScreen function in pyautogui 
it finds where a certain picture is on the screen
"""
def findTarget():
    try:
        global script_directory
        image_path = os.path.join(script_directory, 'target.png')

        target_location = pyautogui.locateCenterOnScreen(image_path)
        return target_location

    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")
        return "not found"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "not found"

def click_on(horizontal_coor, vertical_coor):
    mouse.move(horizontal_coor, vertical_coor, absolute=True)
    mouse.click() 

def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener(main_controller)

if __name__ == "__main__":
    main()