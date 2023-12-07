import pyautogui
import os
import mouse
import sys 


from time import sleep

#allows the import of local folders
sys.path.append('C:\Coding_Projects\Human-Benchmark-AimBot')
from utils.start import *
from utils.screenshot import get_region


#returns if all the targets were clicked on (the save button has appeared)
# def isDone():

script_directory = os.path.dirname(os.path.abspath(__file__))

#area locateCenterOnScreen is looking at
region = get_region()

def main_controller():
    target_location = findTarget()
    while target_location != "not found":
        click_on(target_location.x, target_location.y)
        target_location = findTarget()
    #ends the program
    try:
        keyboard.unhook_all()
    except Exception as e:
        print(f"Error unhooking keyboard: {e}")
    sys.exit()
        

def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    begin_listener(main_controller)

"""
This function takes advantage of the locateOnScreen function in pyautogui 
it finds where a certain picture is on the screen and returns x and y coords
"""
def findTarget(count=0):
    global region

    try:
        global script_directory
        image_path = os.path.join(script_directory, 'target.png')
        target_location = pyautogui.locateCenterOnScreen(image_path, confidence=.35, region=region)
        
        if target_location == None:
            raise Exception(pyautogui.ImageNotFoundException)
        else:
            return target_location
    
    except pyautogui.ImageNotFoundException:
        if(count >= 100):
            return "not found"
        return findTarget(count=count+1)

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