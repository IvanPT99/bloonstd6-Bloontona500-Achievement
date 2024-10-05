import pyautogui
import time

print("The script will start in 10 seconds. Hover over 'continue' after paying the race ticket.")
time.sleep(10)
reps = 500

for i in range(reps):
    print(f"Starting game number {i+1}...")

    pyautogui.click()
    time.sleep(1)

    pyautogui.press('esc')
    time.sleep(1)

print("¡Proccess completed!")