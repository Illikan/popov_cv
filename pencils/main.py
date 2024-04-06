import numpy as np
import cv2

pencils = 0
for i in range(1, 13):
    cur_pensils = 0
    image = cv2.imread(f"img ({i}).jpg",  cv2.IMREAD_GRAYSCALE) 
    thresh = cv2.threshold(image, 120, 255,cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations = 40)
    thresh = cv2.bitwise_not(thresh)

    mask = np.zeros(thresh.shape, dtype="uint8")

    output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)
    (numLabels, labels, stats, centroids) = output
    # loop over the number of unique connected component labels
    for i in range(1, numLabels):
        
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        (cX, cY) = centroids[i]
        
        keepArea = area > 500000 and area < 700000

        if (keepArea):
            cur_pensils += 1
            pencils += 1
    print(f"На картинке {cur_pensils} карандашей")   
    cv2.namedWindow('Output', cv2.WINDOW_NORMAL)
    cv2.imshow("Output", image)
    cv2.waitKey(0)

print(f"На всех картинках {pencils} карандашей")   

