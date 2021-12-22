import slither_api
import pyautogui

def position():
    return slither_api.getmouseposition()

print(position())
