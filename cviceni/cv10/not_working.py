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
import cv2

sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')

from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.functional import *
from my_libs.img.processing import *
from my_libs.img.morphology import *

img_name = "cv10_mince.jpg"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    img = cv2.imread(img_name)
    assert img is not None, "File: " + Blue + img_name + NC + " could not be read, check with os.path.exists()"
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_gray = normalize(img_gray)

    img_segmented = segmentate(img_gray, 135)
    inverted = cv2.bitwise_not(img_segmented)

    # watershed
    # noise removal
    kernel = np.ones((4,4),np.uint8)
    closing = cv2.morphologyEx(inverted,cv2.MORPH_CLOSE,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(closing,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(closing,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.08*dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    #cores = segmentate(dist_transform, 40, invert=True)
    ret, cores = cv2.threshold(dist_transform, 45, 255, 0)
    
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]

    plot_imgs(
        [img, img_segmented, closing, sure_bg, sure_fg, unknown, dist_transform, cores, markers],
        ["Original", "Segmented", "closing", "Sure BG", "Sure FG", "Unknown", "Dist Transform", "Cores", "Markers"],
        cmaps=[None, "gray", "gray", "gray", "gray", "gray", "gray", "gray", "jet"],
        rows=3,
        window_name="WaterShed"
    )

    """
    plot_imgs(
        [img, img_segmented, closed], 
        ["Original", "Segmented", "Closed"],
        cmaps=[None, "gray", "gray"],
        rows=2,
        window_name="WaterShed"
    )
    """
    
    print(Green + "Done." + NC)
