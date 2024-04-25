import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"gitclone\popov_cv\figures_and_colors\balls_and_rects.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
colors_dict_circle = {}
colors_dict_rectangle = {}
output = cv2.connectedComponentsWithStats(gray, 4, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output
for i in range(1, numLabels):
        
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        (cX, cY) = centroids[i]

        smol = imghsv[y:y+h, x:x+w]          
        key = smol[h//2, w//2, 0]
        if(area == w*h):
            if key not in colors_dict_rectangle.keys():
                    colors_dict_rectangle[key] = 1
            else:
                    colors_dict_rectangle[key] += 1     
            
        else:
            if key not in colors_dict_circle.keys():
                    colors_dict_circle[key] = 1
            else:
                    colors_dict_circle[key] += 1
        # cv2.namedWindow("Smol", cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
        # cv2.imshow("Smol" , smol)
        # cv2.waitKey()

print("Количество кругов по оттенкам: ",  colors_dict_rectangle)
print("Количество прямоугольников по оттенкам: ", colors_dict_circle)        
# cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
# cv2.imshow("Image" , gray)
# cv2.waitKey()
plt.imshow(imghsv)
plt.show()