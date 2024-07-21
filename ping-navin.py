import pyautogui, time

time.sleep(2)
while True:
    pyautogui.typewrite("@Navin Shrinivas")
    pyautogui.press("enter")
    pyautogui.keyDown("shift")
    pyautogui.press("enter")
    pyautogui.keyUp("shift")