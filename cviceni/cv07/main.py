# By Pytel

"""
1) Na základě analýzy obrazového histogramu segmentujte objekty (mince) 
v obrázku cv07_segmentace.bmp. Vzhledem k zelenému pozadí by bylo 
vhodné použít barevnou složku g = (G*255)/(R+G+B).  
 
2) Pro identifikaci objektů použijte barvení oblastí (naprogramujte vlastní 
algoritmus, pro odladění použijte např. obrázek cv07_barveni.bmp). Do 
původního obrázku vkreslete těžiště nalezených objektů. 
 
3) Podle velikosti objektů rozpoznejte hodnotu mince, pokud víte, že objekt 
pětikoruny má více než 4000 pixelů a objekt koruny má méně než 4000 pixelů.  
 
4) Vypište výsledek klasifikace: 
tj. např. Na souřadnici těžiště 10,23 se nachází: 5 
 
5) Sečtěte hodnotu mincí a tuto informaci také vypište v konzoli. 

cv07_segmentace.bmp
"""

import sys
import cv2
sys.path.append('../')
from cv04.my_lib import *
from cv03.graphic import *
from my_colors import *

