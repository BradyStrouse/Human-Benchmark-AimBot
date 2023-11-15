import pyautogui
import time
import os
def wait_for_save_button(timeout=60):
    """
    Wait for the "save_button.png" to appear on the screen.

    Parameters:
        timeout (int): Maximum time (in seconds) to wait for the button.

    Returns:
        tuple or None: If the button is found, returns the center coordinates (x, y).
                      If the button is not found within the timeout, returns None.
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, 'save_button.png')
        save_button_location = pyautogui.locateOnScreen(image_path)

        if save_button_location is not None:
            # The button is found; return the center coordinates
            return pyautogui.center(save_button_location)

        # Adjust the sleep duration based on your needs to avoid high CPU usage
        time.sleep(1)

    print("Timeout: Save button not found within the specified time.")
    return None

# Example usage
save_button_coordinates = wait_for_save_button()

if save_button_coordinates is not None:
    print(f"Save button found at coordinates: {save_button_coordinates}")
    # Continue with your code after the button is found
else:
    print("Save button not found within the specified timeout.")
    # Handle the case where the button is not found
