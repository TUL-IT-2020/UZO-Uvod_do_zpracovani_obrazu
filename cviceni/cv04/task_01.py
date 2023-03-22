# By Pytel
import os
import cv2
from my_lib import *

"""
1) Na základě využití jasové korekce odstraňte z obrázků cv04_f01.bmp 
a cv04_f02.bmp poruchy cv04_e01.bmp a cv04_e02.bmp. c = 255. 
"""

porucha = "cv04_f0"
etalon = "cv04_e0"
img_format = ".bmp"

VERBOSE = True

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    for i in range(1,3):
        picture_name = porucha + str(i) + img_format
        etalon_name = etalon + str(i) + img_format
        if VERBOSE:
            print("Picture: ", picture_name)
            print("Etalon: ", etalon_name)
            print("")
        picture_bgr = cv2.imread(picture_name)
        picture_rgb = cv2.cvtColor(picture_bgr, cv2.COLOR_BGR2RGB)
        etalon_bgr = cv2.imread(etalon_name)
        etalon_rgb = cv2.cvtColor(etalon_bgr, cv2.COLOR_BGR2RGB)
        img = intenzity_corecton(picture_rgb, etalon_rgb)
        titles = ["Old", "Etalon", "Corected"]
        plot_imgs([picture_rgb, etalon_rgb, img], titles)

# END