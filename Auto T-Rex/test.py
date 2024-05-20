import cv2
from core import Object

player = Object("Objects\dino.png")

screen = cv2.imread("Screen.png", 0)


# # location = match(screen, player)

# screen = cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR)
# cv2.rectangle(screen, location[0], location[1], (255, 0, 0), 2)


# print(location)
# cv2.imshow('screen', screen)
# cv2.waitKey(0)