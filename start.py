import keyboard
import threading

from humanBenchmark_v05 import main_controller
from humanBenchmark_v05 import running
"""
this file is only used from 0.7 onwards, its just the code that waits to start the program
"""
# initilizes the keyboard threads to begin and end the program
def begin_listener(mainName):
    keyboard.wait("shift")
    # queue the threads
    escape_thread = threading.Thread(target=escape_listener)
    main_thread = threading.Thread(target=mainName)
    # Start all 
    escape_thread.start()
    main_thread.start()
def escape_listener():
    global running
    while not running:
        keyboard.wait("esc")
        running = False
    exit()