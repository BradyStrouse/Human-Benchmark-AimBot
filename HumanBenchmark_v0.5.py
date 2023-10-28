import mss
import keyboard
import threading
import os
import mouse
target_color = "#95c3e8"
start_button = "shift"

monitor = {"top"  : 163 , "left"  : 450
          ,"width": 1000, "height": 500}

#deletes all screenshots taken, 
def delete_screenshots():
    directory = os.getcwd()  # Get the current working directory

    # List all files in the current directory
    file_list = os.listdir(directory)

    # Iterate through the files and delete those starting with "sct"
    for filename in file_list:
        if filename.startswith("sct"):
            os.remove(os.path.join(directory, filename))
            print(f"Deleted: {filename}")

def take_screenshot():
    delete_screenshots()
    with mss.mss() as sct:
        # The screen part to capture
        global monitor
        # #output name
        # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)
        return sct_img
        # Save to the picture file
        # mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
def click_on(horizontal_coor, verticle_coor):
    mouse.move(horizontal_coor, verticle_coor, absolute=True, duration=0)
    mouse.click() 

def find_target():
    global monitor
    screenshot = take_screenshot()
    for verticle in range(monitor["top"], monitor["height"]):
        for horizontal in range(monitor["left"], monitor["width"]):
            if screenshot.pixel(horizontal, verticle) == (149,195,232):
                click_on(horizontal, verticle)



"""
this is where everything is actually put together/
where the main logic happens
"""
def main_controller():
    find_target()

    
def main():
    print("Press SHIFT to begin, press ESCAPE to stop the program")
    wait_to_start()
    find_target()
def escape_listener():
    global running
    keyboard.wait("esc")
    running = False
    print("Emergency escape has been pressed, exiting now")
    exit()

"""
initilizes the keyboard threads to begin and end the program
"""
def wait_to_start():
    keyboard.wait("shift")

    escape_thread = threading.Thread(target=escape_listener)
    main_thread = threading.Thread(target=main_controller)
    # Start all 
    escape_thread.start()
    main_thread.start()

if __name__=="__main__":
    main()