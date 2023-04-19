# By Pytel

"""
1.  Proveďte segmentaci obrázku cv10_mince.bmp, výsledný 
segmentovaný obraz upravte vhodnou morfologickou operací. 
 
2.  Ve výsledném objektu oddělte jednotlivé objekty mincí s využitím 
funkce pro rozvodí (watershed). 
 
3.  Identifikujte objekty mincí pomocí funkce barvení oblastí a spočítejte 
jejich těžiště. Objekty, které byly odděleny transformací rozvodí, a 
které nejsou mincemi neidentifikujte (například na základě velikosti 
objektů). 
 
4.  Těžiště vkreslete do původního RGB obrázku.
"""

import sys

sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')

from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.functional import *
from my_libs.img.processing import *

img_name = "cv10_mince.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    img = cv2.imread(img_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    plt.figure("Mince")
    plt.imshow(img_gray, cmap='gray')
    plt.waitforbuttonpress()
    plt.close()

    
    print(Green + "Done." + NC)
