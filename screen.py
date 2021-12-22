import pyautogui
import numpy
import cv2


def fullScreenCapture():
    capture = pyautogui.screenshot()
    captureArray = numpy.array(capture)
    return captureArray

def partialscreencapture(left,top,width,height):
    capture = pyautogui.screenshot(region = (left,top,width,height))
    capturearray = numpy.array(capture)
    return capture
def grayScaleImage(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale

def invertColor(image):
    inverted = cv2.bitwise_not(image)
    return inverted