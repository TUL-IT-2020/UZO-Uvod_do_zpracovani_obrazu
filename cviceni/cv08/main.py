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

from my_libs.tools import *
from my_libs.colors import *


if __name__ == "__main__":
    clear()

    
    print(Green + "Done." + NC)