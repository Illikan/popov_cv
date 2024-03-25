import numpy as np
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage import draw
from skimage.measure import label
from skimage.filters import threshold_otsu
from collections import defaultdict

def filling_factor(region):
    return np.sum(region.image) / region.image.size

def has_line(region, horizontal = True):
    return 1.0 in np.mean(region.image, int(horizontal)) 

def count_holes(region):
    holes = 0
    labeled = label(np.logical_not(region.image))
    regions = regionprops(labeled)
    for region in regions:
        not_bound = True
        coords = np.where(labeled == region.label)
        for y, x in zip(*coords):
            if y == 0 or x == 0 or y == labeled.shape[0]-1 or x == labeled.shape[1]-1:                
                not_bound = False
        holes +=  not_bound
    return holes

def recognize(region):
    if filling_factor(region) == 1.0:
        return "-"
    else:
        holes = count_holes(region)
        if holes == 2: # B or 8
            if has_line(region, False) and region.image[0, 0] > 0:

                return "B"
            else:
                return "8"
        elif holes == 1:
            if label(np.logical_not(region.image)).max() == 4:
                return "A"
            elif label(np.logical_not(region.image)).max() == 5:
                return "0"
            else:
                # plt.imshow(label(np.logical_not(region.image)))
                # plt.title(f"{holes}")
                # plt.show()
                regions_ = regionprops(label(np.logical_not(region.image)))
                if regions_[0].area == regions_[2].area:
                    # plt.subplot(121)
                    # plt.imshow(label(np.logical_not(regions_[0].image)))
                    # plt.title(f"{regions_[0].area}")
                    # plt.subplot(122)
                    # plt.imshow(label(np.logical_not(regions_[2].image)))
                    # plt.title(f"{regions_[2].area}")
                    # plt.show()
                    return "D"
                else:
                    return "P"
        else:
            if has_line(region, False):
                return "1"
            if has_line(region):
                plt.imshow(region.image)
                plt.show()
                return "*"
            inv = np.logical_not(region.image)
            labeled = label(inv)
            holes = labeled.max()
            match holes:
                case 2:
                    return "/"
                case 4: 
                    return "X"
                case 5: 
                    return "W"
                case _: 
                    return "__"
    return "_"


image = plt.imread(r"C:\Users\ze_us\Documents\VSProjects\Computer_vision_2sem\10les_23.03\symbols.png")
image = np.mean(image, 2)
image[image > 0] = 1

labeled = label(image)
symbols = labeled.max()
regions = regionprops(labeled)
result = defaultdict(lambda: 0)


for region in regionprops(labeled):
    result[recognize(region)] += 1
print(result)
#plt.title(f"Holes = {count_holes(regions[nfig])}")
#plt.imshow(regions[nfig].image)
plt.show()