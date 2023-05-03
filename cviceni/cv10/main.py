# By Pytel, mothspaws

"""
1. Proveďte segmentaci obrázku cv10_mince.bmp, výsledný segmentovaný obraz 
upravte vhodnou morfologickou operací.

2. Ve výsledném objektu oddělte jednotlivé objekty mincí s využitím funkce pro rozvodí (watershed).

3. Identifikujte objekty mincí pomocí funkce barvení oblastí a spočítejte jejich těžiště. 

Objekty, které byly odděleny transformací rozvodí, a které nejsou mincemi neidentifikujte 
(například na základě velikosti objektů).

4. Těžiště vkreslete do původního RGB obrázku.
"""
import sys
import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')

from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.processing import *

img_name = "cv10_mince.jpg"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    # Read the image and convert it to grayscale
    img = cv2.imread(img_name)
    assert img is not None, "File: " + Blue + img_name + NC + " could not be read, check with os.path.exists()"
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Apply thresholding
    ret, thresh = cv2.threshold(img_gray, 130, 255, 0)

    # Invert the thresholded image
    thresh = cv2.bitwise_not(thresh)

    # Perform morphological operations
    kernel = np.ones((6, 6), np.uint8)

    # Closing
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    # closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)


    # Remove small white regions
    sure_bg = cv2.dilate(closing, kernel, iterations=3)

    # Distance transform and normalization
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Subtract the sure foreground from the sure background
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    # Apply watershed
    markers = cv2.watershed(img, markers)

    # Calculate centroids
    label_array, num_features = ndimage.label(sure_fg)
    centroid_list = ndimage.center_of_mass(sure_fg, label_array, range(1, num_features + 1))

    # Draw centroids on the original image
    for centroid in centroid_list:
        cv2.circle(img, (int(centroid[1]), int(centroid[0])), 5, (0, 255, 0), -1)

    # Display the result

    plot_imgs(
        [img_gray, thresh, closing, sure_bg, dist_transform, sure_fg, unknown, markers, img],
        ["Původní", "Adaptivní prahování", "Uzavření", "Označení pozadí", "Transformace vzdálenosti", "Označení popředí", "Neznámé", "Vodní rozvodí", "Výsledek"],
        rows=3,
        cmaps=[None, "gray", "gray", "gray", "gray", "gray", "gray", "gray", None],
        cbars=[False, False, False, False, False, False, False, False, False],
        figsize=(12, 12),
        window_name="Watershed"
    )
    
    print(Green + "Done." + NC)
