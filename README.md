# Auto Bloons Script

This script automates the process of entering and exiting a career game in Bloons TD6 to unlock the achievement of participating 500 times in the career mode. The script uses `pyautogui` to simulate clicks and the `Esc` key.

## Requirements

To ensure the script works correctly, you need to have the following dependencies installed:

1. [Python](https://www.python.org/downloads/) (any modern version should work).
2. The Python libraries `pyautogui` and `keyboard`. You can install them with:
   pip install pyautogui keyboard

## Usage of the Script
1. Open the game Bloons TD6 and get ready to enter career mode. You will need to get one RACE TICKET with ilimitated tries.
2. Run the script from your terminal or Python environment. (You have 10 seconds to position the mouse over the "Continue" button in the menu.)
3. You can stop the script at any time by pressing the x key.

## Execution
You can run the script with Python from the terminal or command line:

   python auto_bloons.py

The script will automatically start clicking the "Continue" button for 500 repetitions or until you press x to stop it!

## Stopping the Script
At any time during the execution of the script, you can press the x key to stop the process.

## Notes
Make sure to have the game in fullscreen or windowed mode without moving it while the script is running, as the script will click at the position where you are with the mouse.
You can modify the number of repetitions by adjusting the repetitions variable in the source code.