import os
import mss


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

def delete_potential():
    directory = os.getcwd()  # Get the current working directory

    # List all files in the current directory
    file_list = os.listdir(directory)

    # Iterate through the files and delete those starting with "sct"
    for filename in file_list:
        if filename.startswith("pot"):
            os.remove(os.path.join(directory, filename))



target_count = 0
def screenshot_area(x, y):
    # delete_potential()
    global target_count
    target_count +=1
    monitor = {"top"  : x , "left"  : y
          ,"width": 100, "height": 100}
    with mss.mss() as sct:
        #output name
        output = "potiential_target" + str(target_count) + ".png"

        # Grab the data
        sct_img = sct.grab(monitor)
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return sct_img
    

def take_screenshot():
    delete_screenshots()
    with mss.mss() as sct:
        # The screen part to capture
        global monitor
        #output name
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return sct_img

if __name__ == "__main__":
    delete_potential()
    delete_screenshots()