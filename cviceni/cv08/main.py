# By Pytel, mothspaws

"""
Segmentujte  obrázky  cv08_im1.bmp  a  cv08_im2.bmp  dle  vhodně 
stanoveného prahu. 
 
2.  Pro  filtrování  binárních  obrázků  použijte  metodu  otevření  nebo 
uzavření (pokud to bude nutné!), velikost strukturních elementů volte 
pomocí mezivýsledku ze segmentace. 
 
3.  Výsledkem by měl být binární obraz se 4 kruhovými objekty. 
 
4.  Pro identifikaci objektů použijte algoritmus barvení objektů. 
 
5.  Pro každý identifikovaný objekt vypočtěte těžiště a souřadnice těžiště 
vyznačte  v původním  barevném  obrázku  pomocí  zeleného  křížku, 
hvězdy....

Erozi a dilatace, funkce z opencv.
Černý obrázek vyřešit pomocí morfologických operací.

Červený bez morfologické operace, stačí správný barevný prostor.
"""

import cv2
import sys

sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')

from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.functional import *
from my_libs.img.processing import *

DEBUG = False

img_black = "cv08_im1.bmp"
img_red = "cv08_im2.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    # BLACK
    img = cv2.imread(img_black)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if DEBUG:
        plt.figure("Histogram")
        plt.hist(img_gray.ravel(), bins=256, range=(0, 256))
        plt.waitforbuttonpress()
        plt.close()
    img_gray = segmentate(img_gray, 80, invert=True)
    radius = 6
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (radius, radius))
    if DEBUG:
        print("Kernel: \n", kernel)
    img_morphed = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)

    # inverze kvuli barveni objektu
    img_inverted = cv2.bitwise_not(img_morphed)
    colored, numbers = color_objects(img_inverted)
    if DEBUG:
        print("Numbers:", numbers)
        plt.figure("Colored objects")
        plt.imshow(colored)
        plt.waitforbuttonpress()
        plt.close()

    centers = calculate_centers_of_objects(colored, numbers)

    plot_imgs_x([img, img_gray, img_morphed, img], 
              ["img", "gray", "morhed", "centers"], 2, 
              cmaps=[None, "gray", "gray", None],
              centers=centers,
              window_name="Image with black dots"
    )

    # RED
    img = cv2.imread(img_red)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    r_color_space = img_to_r(img)
    r_color_space = normalize(r_color_space)
    
    if DEBUG:
        plt.figure("Histogram")
        plt.hist(r_color_space.ravel(), bins=256, range=(0, 256))
        plt.waitforbuttonpress()
        plt.close()

    r_segmented = segmentate(r_color_space, 100, invert=False)
    colored, numbers = color_objects(r_segmented)
    centers = calculate_centers_of_objects(colored, numbers)
    plot_imgs_x([img, r_color_space, r_segmented, img], 
              ["img", "red", "segmented", "centers"], 2, 
              cmaps=[None, 'jet', 'gray', None],
              centers=centers,
              window_name="Image with red dots",
              points=(233, 150, 122)
    )

    print(Green + "Done." + NC)