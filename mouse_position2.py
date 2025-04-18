import pyautogui
import time

def position(time_s):
    try:        
        x, y = pyautogui.position()
        print(f"滑鼠位置：({x}, {y})")
        time.sleep(time_s)
    except KeyboardInterrupt:
        print("\n已停止")

print("持續查看滑鼠位置,按 Ctrl+C 中止")
while True:
    position(0.5)
