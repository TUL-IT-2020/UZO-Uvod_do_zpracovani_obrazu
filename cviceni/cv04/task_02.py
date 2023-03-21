# By Pytel
import os
import cv2
from my_lib import *

"""
2) Pro obrázek cv04_rentgen.bmp naprogramujte ekvalizaci histogramu 
dle:

q0, p0 = 0 a qk = 255 
 
Zobrazte původní  a  ekvalizovaný  obrázek  spolu  s příslušnými histogramy.
"""

rentgen = "cv04_rentgen.bmp"

if __name__ == '__main__':
    plt.ion()
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    elif os.name == 'posix':
        clear = lambda: os.system('clear')
    clear()
    plt.close('all')
    
    rentgen_bgr = cv2.imread(rentgen)
    rentgen_rgb = cv2.cvtColor(rentgen_bgr, cv2.COLOR_BGR2RGB)
    gray_rentgen = cv2.cvtColor(rentgen_rgb, cv2.COLOR_RGB2GRAY)
    ekv_rentgen = ekvalise(gray_rentgen)
    
    plt.subplot(2, 2, 1)
    plt.title("Old rentgen")
    plt.imshow(rentgen_rgb)
    plt.subplot(2, 2, 2)
    plt.title("Hist of rentgen")
    hist = histogram(rentgen_rgb)
    #hist = histogram(gray_rentgen)
    #hist = histogram(gray_rentgen.astype('uint8'))
    #hist = np.histogram(rentgen_rgb, bins=256)[0]
    plt.plot(np.arange(hist.shape[0]), hist)
    
    plt.subplot(2, 2, 3)
    plt.title("Corrected rentgen")
    #plt.imshow(ekv_rentgen.astype('uint8'), cmap='gray')
    plt.imshow(ekv_rentgen, cmap='gray')
    plt.subplot(2, 2, 4)
    plt.title("Corrected hist of rentgen")
    hist = histogram(ekv_rentgen)
    #hist = np.histogram(ekv_rentgen.astype('uint8'), bins=256)[0]
    plt.plot(np.arange(hist.shape[0]), hist)
    plt.show()
    plt.waitforbuttonpress()

# END