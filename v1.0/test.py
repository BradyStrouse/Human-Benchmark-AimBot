import os
import pyautogui
pyautogui.screenshot('target.png')
# file_path = "C:\Coding_Projects\Human-Benchmark-AimBot\\v1\\target.png"

# # Check if the file exists
# if os.path.exists(file_path):
#     # Get the file permissions
#     permissions = os.stat(file_path).st_mode

#     # Check read permission
#     if permissions & 0o100:
#         print(f"The file {file_path} has read permission.")
#     else:
#         print(f"The file {file_path} does not have read permission.")
# else:
#     print(f"The file {file_path} does not exist.")