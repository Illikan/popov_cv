from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

def area(LB, label = 1):
    return np.sum(LB == label)

def zone_3x3(LB, y, x):
    return [[LB[y-2, x-2], LB[y-2, x], LB[y-2, x+2]],
            [LB[y, x-2], LB[y, x], LB[y, x+2]],
            [LB[y+2, x-2], LB[y+2, x], LB[y+2, x+2]]]


image = np.load(r"C:\Users\ze_us\Documents\VSProjects\Computer_vision_2sem\Homework\figures\ps.npy.txt")
labeled = label(image)
all_figures = labeled.max()
fig_list = []
fig_dict = {}

#Получаем список всех структурирующих элементов 3х3 в которых серединный элемент не нулевой
for y in range(2, labeled.shape[0] -4):
    for x in range(2, labeled.shape[1] - 4):
        if image[y, x]  != 0:
            zone = zone_3x3(image, y, x)
            if np.sum(zone) == 5:
                fig_list.append(zone)

#Получаем из них словарь в котором уникальные структурирующие элементы - ключи, а значения - количество соответствующих элементов
for arr in np.unique(fig_list, axis=0):
    fig_dict[tuple(map(tuple, arr))] = 0
 
#Для каждого маркированного элемента проверяем, является ли он одним из найденных нами элементов и если да, то прибавляем к соответсвующему элементу словаря 1   
for i in range(1, all_figures+1):
    for arr in np.unique(fig_list, axis=0):
        check = labeled == i
        if np.array_equal(check, binary_erosion(check, arr)):
            fig_dict[tuple(map(tuple, arr))] += 1

# На моем ноутбуке итоговое время выполнения составляет больше 40 секунд, мне больно, я даже не могу проверить работает ли программа тк не хватает терпения ждать)