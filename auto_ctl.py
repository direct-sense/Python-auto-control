import pyautogui
import pygetwindow as gw
import time

window_title = "LINE"
window = gw.getWindowsWithTitle(window_title)[0]

window.activate()
time.sleep(1)

#pyautogui.click(window.left + 100, window.top + 100)
pyautogui.write("Hello from pyautogui!")
pyautogui.press("tab")
pyautogui.write("Hello from pyautogui!")
pyautogui.press("enter")
