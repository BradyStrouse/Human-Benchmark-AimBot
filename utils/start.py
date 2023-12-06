import keyboard
import threading
import sys 

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
    # escape_thread.start()
    main_thread.start()
def escape_listener():
    keyboard.wait("esc")
    keyboard.unhook_all()
    print("settings to false")
    # set_running(False)
    sys.exit(0)

def printsomething():
    print("hello world")

if __name__ == "__main__":
    begin_listener(printsomething)