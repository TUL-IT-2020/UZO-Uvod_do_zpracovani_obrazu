# By Pytel

"""
1) Na základě analýzy obrazového histogramu segmentujte objekty (mince) 
v obrázku cv07_segmentace.bmp. Vzhledem k zelenému pozadí by bylo 
vhodné použít barevnou složku g = (G*255)/(R+G+B).

PDF strana 10+.

2) Pro identifikaci objektů použijte barvení oblastí (naprogramujte vlastní 
algoritmus, pro odladění použijte např. obrázek cv07_barveni.bmp). Do 
původního obrázku vkreslete těžiště nalezených objektů.
 
3) Podle velikosti objektů rozpoznejte hodnotu mince, pokud víte, že objekt 
pětikoruny má více než 4000 pixelů a objekt koruny má méně než 4000 pixelů.  
 
4) Vypište výsledek klasifikace: 
tj. např.: "Na souřadnici těžiště 10,23 se nachází: 5" 
 
5) Sečtěte hodnotu mincí a tuto informaci také vypište v konzoli. 

cv07_segmentace.bmp
"""

import sys
import cv2
sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')
from my_libs.fft import *
from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.processing import *
from my_libs.img.functional import *



def calculate_centers_of_objects(img, object_numbers = [1]) -> dict:
    """ Calculate centers of objects in image.

    Args:
        img: image, where objects are marked by numbers
        object_numbers: list of numbers of objects
    
    Return: 
        dict of centers
    """
    X, Y = img.shape
    moments = [(1,0), (0,1), (0,0)]

    centers = {}
    for object_number in object_numbers:
        centers[object_number] = [0, 0, 0]
    
    for x in range(X):
        for y in range(Y):
            number = img[y][x]
            if number not in object_numbers:
                continue
            for index, moment in enumerate(moments):
                centers[number][index] += x**moment[0] * y**moment[1]

    for key in centers:
        centers[key][0] /= centers[key][2]
        centers[key][1] /= centers[key][2]

    return centers

mince = "cv07_segmentace.bmp"
barveni = "cv07_barveni.bmp"

if __name__ == "__main__":
    plt.ion()
    clear()
    plt.close('all')

    img_file_name = mince
    if not os.path.isfile(img_file_name):
        raise FileNotFoundError(Red + "File:", Blue + str(img_file_name), Red + "not found!" + NC)

    # Load image:    
    img = cv2.imread(img_file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # convert to g:
    g = img_to_g(img)
    print(np.max(g), np.min(g))
    g = normalize(g)
    print(np.max(g), np.min(g))

    # Show image:
    plt.figure("Image")
    plt.imshow(g, cmap='jet')
    #plt.imshow(g, cmap='gray')
    plt.waitforbuttonpress()

    # Histogram:
    plt.figure("Histogram")
    plt.hist(g.ravel(), bins=256, range=(0, 256))
    plt.waitforbuttonpress()
    # TODO: spociat hodnotu T !!!
    T = 100

    # Segmentate image:
    g = segmentate(g, T, 255)
    plt.figure("Segmentated image")
    plt.imshow(g, cmap='gray')
    plt.waitforbuttonpress()

    # Colored objects:
    colored, number = color_objects(g)
    plt.figure("Colored objects")
    plt.imshow(colored, cmap='jet')
    plt.waitforbuttonpress()

    # Calculate centers:
    centers = calculate_centers_of_objects(colored, range(1, number+1))

    # Detect objects:

    # Nalezené objekty:
    #print("Na souřadnici těžiště", 10,23, "se nachází:", 5)
    # Suma mincí:
    #print("Suma hodnot mincí:", 5)
    
    print(Green + "Done." + NC)
    
# END