import pyautogui
import numpy
import screen
import ocr
import numpy as np
import cv2


def getmouseposition():
    return pyautogui.position()

def begingame():
    pyautogui.click(x=956 ,y=620)

def movetoTop():
    pyautogui.moveTo(958,374)

def movetoDown():
    pyautogui.moveTo(960,613)

def movetoRight():
    pyautogui.moveTo(1330,570)

def movetoLeft():
    pyautogui.moveTo(730,553)

def movetoTopRight():
    pyautogui.moveTo(1199,392)

def movetoTopLeft():
    pyautogui.moveTo(753,426)

def movetoBottomLeft():
    pyautogui.moveTo(800,670)

def movetoBottomRight():
    pyautogui.moveTo(1135,670)

def readfinalscore():
    capture = screen.partialscreencapture(831, 413, 256, 40)  # top left width height
    text = ocr.read(capture)
    score = "".join(filter(str.isdigit, text))
    if (score == ""):
        score = "-1"
    finalScore = int(score)
    return finalScore

def readcurrentscore():
    capture = screen.partialscreencapture(1, 987, 135, 25)  # top left width height
    text = ocr.read(capture)
    score = "".join(filter(str.isdigit, text))
    if (score == ""):
        score = "-1"
    finalScore = int(score)
    return finalScore
def isplaying():
    if(readcurrentscore() == -1):
        return False
    return True

def endedgame():
    if(readcurrentscore() == -1):
        return True
    return False
def returngamescreen(width,height):
    gameScreen = screen.partialscreencapture(74, 0, 1912, 1031)
    #585, 286, 825, 491

    gameScreen = np.array(gameScreen)
    gameScreen = cv2.resize(gameScreen, (width, height))
    gameScreen = screen.grayScaleImage(gameScreen)
    gameScreen = np.expand_dims(gameScreen, -1)
    return gameScreen








