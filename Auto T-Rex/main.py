import cv2
import mss
import matplotlib.pyplot as plt
import pyautogui as pag
import time
import numpy as np
from PIL import Image

# Начало измерения времени
start_time = time.time()
# Переменная для первого скриншота, потом убрать
jumped = 0
# Переменная для симуляции ускорения
x = 0    
# Берем скриншот первый раз и превращаем его в массив numpy
image = pag.screenshot(region=[660,170,600,150])
img = np.array(image)
# print(img[132, 53:185, 2])
# plt.imshow(img[50, 250:260])
# plt.show()
# Цикл пока не геймовер
while img[50, 253, 2] != 83:
    # pag.keyDown('down')
    
    # Взали скриншот и превратили в массив
    image = pag.screenshot(region=[660,170,600,150])
    img = np.array(image)
    # Отмерили сколько прошло времени
    another_time = time.time()
    cur_time = another_time - start_time
    # Какая-то формула чтобы симулировать ускорение, но она ебаная и бесит меня тк рандомная и нихуя не работает сука
    x = int(cur_time*(1+cur_time/100))
    # Если в прямоугольнике перед динозавром нашли пиксель препятствия то прыгаем, зона постоянно расширяется по ебаной формуле, которая ебаная и я устал сука
    if  (img[100:132, 70+int(x/4):185+x, 2] == 83).any():
        # if img[122, 27, 2] == 83:
        # pag.keyUp("down")
        pag.press(" ")
        if not jumped:
            image.save("saved_first jump.jpg")
            jumped = 1        
        image.save("saved_last_jump.jpg")
        # cv2.namedWindow('Output', cv2.WINDOW_NORMAL)
        # cv2.imshow("Output", img)
        # cv2.waitKey(0)
print(cur_time)
print(1+cur_time/100 - 0.2)
plt.imshow(img)
plt.show()