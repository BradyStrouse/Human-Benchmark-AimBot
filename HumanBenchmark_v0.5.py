import mss

#these are coords of the top left and bottom right respectivily 
region = (515 , 200
        , 1500, 650)
with mss.mss() as sct:
    # Capture the screenshot of the specified region
    screenshot = sct.shot(output="sc.png", output_as="png", rect=region)

screenshot = sct.shot(output="C:\Coding projects\Human-Benchmark-AimBot", rect=region)