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

img_b = "cv09_bunkyB.bmp"
img_c = "cv09_bunkyC.bmp"
img_rice = "cv09_rice.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')