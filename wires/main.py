from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

image = np.load(r"C:\Users\ze_us\Documents\VSProjects\Computer_vision_2sem\7les_09.03\wires6npy.txt")

labeled = label(image)
number = label(image, return_num=True)[1]

plt.imshow(labeled)
plt.show()

for i in range(1, number+1):
    im = (labeled == i)
    im = binary_erosion(im)
    count = np.max(label(im))
    
    match(count):
        case 1:
            print(f"{i}-ый провод не порван")
        case 0:
            print(f"{i}-ый провод полноcтью порван")
        case _:
            print(f"{i}-ый провод порван на {count} кусков")

