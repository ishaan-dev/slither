import cv2
import screen
import slither_api
import numpy as np
gameScreen = screen.partialscreencapture(74, 0, 1912, 1031)
gameScreen = np.array(gameScreen)


cv2.imshow("im1" , gameScreen)
cv2.waitKey(0)







