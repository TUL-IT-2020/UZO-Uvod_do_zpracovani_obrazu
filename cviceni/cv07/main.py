# By Pytel, mothspaws

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
from my_libs.img.functional import *
from my_libs.img.processing import *
from my_libs.colors import *
from my_libs.tools import *
import cv2
import sys
DEBUG = False


sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')
if DEBUG:
    for path in sys.path:
        print(path)
    input()


def calculate_centers_of_objects(img, object_numbers=[1]) -> dict:
    """ Calculate centers of objects in image.

    Args:
        img: image, where objects are marked by numbers
        object_numbers: list of numbers of objects

    Return: 
        dict of centers
    """
    X, Y = img.shape
    moments = [(1, 0), (0, 1), (0, 0)]

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
        raise FileNotFoundError(Red + "File:", Blue +
                                str(img_file_name), Red + "not found!" + NC)

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

    # Na základě analýzy histogramu byl vybrán prah T
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

    # Draw centers:
    img_centers = img.copy()
    for key in centers:
        center = (int(centers[key][0]), int(centers[key][1]))
        cv2.circle(img_centers, center, 5, (255, 0, 0), -1)

    plt.figure("Image with centers")
    plt.imshow(img_centers)
    plt.show(block=False)
    plt.pause(0.001)

    # Detect objects:
    coins = []
    coords = []
    threshold = 4000
    for key in centers:
        print(key, centers[key])
        # detect coins:
        if centers[key][2] > threshold:
            coins.append(5)
        else:
            coins.append(1)
        # position:
        coords.append((centers[key][0], centers[key][1]))

    # Print results:
    for i in range(len(coins)):
        print("Na souřadnici těžiště", coords[i], "se nachází:", coins[i])

    coins_value_sum = sum(coins)
    print("Suma hodnot mincí:", coins_value_sum)

    print(Green + "Done." + NC)

# END
