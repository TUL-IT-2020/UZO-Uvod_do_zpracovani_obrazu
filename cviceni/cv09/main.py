# By Pytel

"""
1. Z obrázků cv09_bunkyB.bmp a cv09_bunkyC.bmp odstraňte drobný bílý 
(černý) šum při využití šedotónových morfologických transformací 
otevření a uzavření.  
 
strukturní element volte:   
    [[0, 1, 0], 
     [1, 1, 1]] 
 
2.  Využijte operaci top-hat (vrchní část klobouku) pro předzpracování 
obrazu cv09_rice.bmp.  
 
3.  Segmentujte původní a upravený obraz vhodně stanoveným prahem. 
 
4.  Spočítejte počet zrn v původním a upraveném segmentovaném obraze. 
Stanovte si například práh, že objekty menší než 100 pixelů nejsou celými 
zrnky. Vypište do konzole výsledek, např.: 
 
Pocet zrnicek ryze na obrazku: 90 

5.  Identifikujte jednotlivé objekty (zrníčka), spočítejte jejich těžiště a 
vkreslete jejich pozice do původního obrázku: 
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
from my_libs.img.morphology import *

img_b_name = "cv09_bunkyB.bmp"
img_c_name = "cv09_bunkyC.bmp"
img_rice_name = "cv09_rice.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    kernel = np.array([
        [0, 1, 0], 
        [1, 1, 1]], 
        dtype=np.uint8
    )

    """
    kernel = np.array([
        [0, 1, 0], 
        [1, 2, 1], 
        [0, 1, 0]], 
        dtype=np.uint8
    )"""

    # Buňky
    img_b = cv2.imread(img_b_name)
    img_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB)
    img_b_gray = cv2.cvtColor(img_b, cv2.COLOR_RGB2GRAY)    
    
    img_b_erodet = morphology(img_b_gray, MorphologyOperation.GRAY_ERODE, kernel)
    img_b_dilated = morphology(img_b_erodet, MorphologyOperation.GRAY_DILATE, kernel)
    #img_b_erodet = cv2.morphologyEx(img_b_gray, cv2.MORPH_ERODE, kernel)
    #img_b_dilated = cv2.morphologyEx(img_b_erodet, cv2.MORPH_DILATE, kernel)

    img_c = cv2.imread(img_c_name)
    img_c = cv2.cvtColor(img_c, cv2.COLOR_BGR2RGB)
    img_c_gray = cv2.cvtColor(img_c, cv2.COLOR_RGB2GRAY)

    img_c_dilated = morphology(img_c_gray, MorphologyOperation.GRAY_DILATE, kernel)
    img_c_erodet = morphology(img_c_dilated, MorphologyOperation.GRAY_ERODE, kernel)

    plot_imgs(
        [img_b_gray,img_b_erodet,img_b_dilated, img_c_gray,img_c_dilated,img_c_erodet],
        ["Původní -> otevření","Eroze","Dilatace", "Původní -> uzavření","Dilatace","Eroze"],
        2,
        ["gray", "gray", "gray", "gray", "gray", "gray"],
        window_name="Bunky"
    )

    # Rice
    img_rice = cv2.imread(img_rice_name)
    img_rice = cv2.cvtColor(img_rice, cv2.COLOR_BGR2RGB)
    img_rice_gray = cv2.cvtColor(img_rice, cv2.COLOR_RGB2GRAY)
    
    kernel = np.ones((15, 15), np.uint8) #15 x 15
    #kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(15,15)) #10 20
    #kernel = cv.getStructuringElement(cv.MORPH_CROSS,(25,21)) #10 20
    
    img_rice_segmented = segmentate(img_rice_gray, 135)
    img_rice_top_hat = morphology(img_rice_gray, MorphologyOperation.GRAY_TOP_HAT, kernel)
    #img_rice_top_hat = cv2.morphologyEx(img_rice_gray, cv2.MORPH_TOPHAT, kernel)
    img_rice_top_hat_segmented = segmentate(img_rice_top_hat, 60)

    plot_imgs(
        [img_rice,img_rice,img_rice_segmented, img_rice_top_hat,img_rice_top_hat,img_rice_top_hat_segmented],
        ["Původní","Histogram","Segmentace", "Top hat","Histogram","Segmentace"],
        2,
        ["gray", None, "gray", "gray", None, "gray"],
        hist=[None, True, None, None, True, None],
        window_name="Rýže"
    )
    
    rice_inverted = cv2.bitwise_not(img_rice_top_hat_segmented)
    colored, numbers = color_objects(rice_inverted)
    centers_dict = calculate_centers_of_objects(colored, numbers)
    
    centers_list = []
    for key in centers_dict:
        area = centers_dict[key][2]
        x = centers_dict[key][0]
        y = centers_dict[key][1]
        if area > 100:
            centers_list.append([x, y])
    print("Number of detected objects:", Blue + str(len(centers_list)) + NC + ".")
    
    centers = np.array(centers_list, dtype=np.int32)
    #plt.imshow(img_rice_top_hat_segmented)
    plt.scatter(centers[:, 1], centers[:, 0], marker="x", color="red", s=10)
    plt.set_cmap("gray")
    plt.show()
    plt.waitforbuttonpress()
    
    print(Green + "Done." + NC)
