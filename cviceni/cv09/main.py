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

img_b_name = "cv09_bunkyB.bmp"
img_c_name = "cv09_bunkyC.bmp"
img_rice_name = "cv09_rice.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    # Buňky
    img_b = cv2.imread(img_b_name)
    img_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB)
    img_b_gray = cv2.cvtColor(img_b, cv2.COLOR_RGB2GRAY)

    plt.figure("Bunky")
    plt.imshow(img_b_gray, cmap='gray')
    plt.waitforbuttonpress()
    plt.close()

    kernel = np.array([
        [0, 1, 0], 
        [1, 1, 1]], dtype=np.uint8
    )
    
    # TODO: šedotónové morfologické transformace
    img_b_erodet = cv2.erode(img_b_gray, kernel)
    img_b_dilated = cv2.dilate(img_b_erodet, kernel)


    img_c = cv2.imread(img_c_name)
    img_c = cv2.cvtColor(img_c, cv2.COLOR_BGR2RGB)
    img_c_gray = cv2.cvtColor(img_c, cv2.COLOR_RGB2GRAY)

    img_c_dilated = cv2.dilate(img_c_gray, kernel)
    img_c_erodet = cv2.erode(img_c_dilated, kernel)

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

    """
    plt.figure("Rice")
    plt.imshow(img_rice_gray, cmap='gray')
    plt.waitforbuttonpress()
    plt.close()
    """

    print(Green + "Done." + NC)