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
    """
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
    #"""

    # Rice
    img_rice = cv2.imread(img_rice_name)
    img_rice = cv2.cvtColor(img_rice, cv2.COLOR_BGR2RGB)
    img_rice_gray = cv2.cvtColor(img_rice, cv2.COLOR_RGB2GRAY)
    
    
    
    img_rice = cv2.imread(img_rice_name)
    img_rice = cv2.cvtColor(img_rice, cv2.COLOR_BGR2RGB)
    img_rice_gray = cv2.cvtColor(img_rice, cv2.COLOR_RGB2GRAY)
    """
    output_adapthresh = cv2.adaptiveThreshold(img_rice_gray, 255.0, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, -20.0)
    kernel = np.ones((5,5),np.uint8)
    output_erosion = cv2.erode(output_adapthresh, kernel)

    contours, _ = cv2.findContours(output_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_contour = cv2.cvtColor(img_rice_gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
    print("Number of detected contours", len(contours))
    cv2.imshow("Original", output_contour)
    cv2.imshow("Rice", img_rice)
    plt.waitforbuttonpress()
    #"""

    img_rice_segmented = segmentate(img_rice_gray, 135)
    #img_rice_top_hat = morphology(img_rice_gray, MorphologyOperation.GRAY_TOP_HAT, kernel)
    #img_rice_gray = cv2.bitwise_not(img_rice_gray)
    img_rice_top_hat = cv2.morphologyEx(img_rice_gray, cv2.MORPH_TOPHAT, kernel)
    img_rice_top_hat_segmented = segmentate(img_rice_top_hat, 10)

    plot_imgs(
        [img_rice,img_rice,img_rice_segmented, img_rice_top_hat,img_rice_top_hat,img_rice_top_hat_segmented],
        ["Původní","Histogram","Segmentace", "Top hat","Histogram","Segmentace"],
        2,
        ["gray", None, "gray", "gray", None, "gray"],
        hist=[None, True, None, None, True, None],
        window_name="Rýže"
    )
    #"""
    print(Green + "Done." + NC)
