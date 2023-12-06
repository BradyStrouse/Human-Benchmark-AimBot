import os
import mss

# this is the area I have defined as the play area (could change with different resolutions)
monitor = {"top"  : 163 , "left"  : 450
          ,"width": 1000, "height": 500}

#area defined by (left, top, width, height)
region = (450, 163, 1000, 500)


target_count = 0
def screenshot_area(x, y, width, height, save_sc = False):
    # delete_potential()
    global target_count
    target_count +=1
    monitor = {"top"  : x , "left"  : y
          ,"width": width, "height": height}
    with mss.mss() as sct:
        # Grabs the data
        sct_img = sct.grab(monitor)

        if save_sc:
            output = "potiential_target" + str(target_count) + ".png"
            # Saves the picture to a file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        return sct_img
    
# simple screenshot, already defined area for 1080p
def take_screenshot():
    return screenshot_area(monitor["top"], monitor["left"], monitor["width"], monitor["height"])


#deletes all screenshots taken (used for beta testing) 
def delete_screenshots():
    directory = os.getcwd()  # Get the current working directory

    # List all files in the current directory
    file_list = os.listdir(directory)

    # Iterate through the files and delete those starting with "sct"
    for filename in file_list:
        if filename.startswith("sct"):
            os.remove(os.path.join(directory, filename))
            print(f"Deleted: {filename}")



#deletes the target specific screenshots (used for beta testing)
def delete_potential():
    directory = os.getcwd()  # Get the current working directory

    # List all files in the current directory
    file_list = os.listdir(directory)

    # Iterate through the files and delete those starting with "sct"
    for filename in file_list:
        if filename.startswith("pot"):
            os.remove(os.path.join(directory, filename))


def get_region():
    global region
    return region

if __name__ == "__main__":
    take_screenshot()