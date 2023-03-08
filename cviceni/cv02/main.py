# By Pytel

"""
1) Naprogramujte algoritmus CamShift pro sledování objektu hrnečku
v obraze videa cv02_hrnecek.mp4
2) Vzor pro sledování objektu je uložen v obrázku cv02_vzor_hrnecek.bmp.
3) Naprogramujte nejprve algoritmus bez využití sledování.
4) Potřebné funkce můžete nalézt ve scriptu - cv02-init.py. Řazení funkcí a jejich logika není stejná jako v požadovaném algoritmu!
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

pattern_file = "cv02_vzor_hrnecek.bmp"
video_file = "cv02_hrnecek.mp4"

def CamShift():
    pass

def rgb2hsv_histogram(rgb):
    """ Convert RGB image to HSV histogram
    """
    # RGB to HSV
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hue = hsv[:,:,0]

    # Histogram
    hist, b = np.histogram(hue, bins=256, range=(0, 256))

    # normalize histogram
    hist = hist / np.max(hist)

    return hist

def histogram_center(hist):
    """ Calculate center of histogram
    """
    pass
    

def process_image(image):
    """ Process image
    """
    bgr = cv2.imread(image)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hist = rgb2hsv_histogram(rgb)

    # picure size
    print("Image size: {0}".format(rgb.shape))
    
    # Plot
    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(rgb)
    plt.subplot(1, 3, 2)
    plt.imshow(hsv)

    plt.subplot(1, 3, 3)
    plt.plot(hist)
    plt.title("Histogram")
    plt.xlabel("Hue")
    plt.ylabel("Count")

    plt.show()
    plt.waitforbuttonpress()

if __name__ == "__main__":
    plt.ion()
    #clear = lambda: os.system('cls')
    clear = lambda: os.system('clear')
    clear()
    plt.close('all')

    cap = cv2.VideoCapture(video_file)

    # Velikost ze vzoru
    patern_rgb = cv2.imread(pattern_file)
    x, y, z = patern_rgb.shape

    patern_hue_hist = rgb2hsv_histogram(patern_rgb)

    while True:
        ret, bgr = cap.read()
        if not ret:
            break
        hsv = cv2.cvtColor(bgr, cv2.COLOR_RGB2HSV)
        hue = hsv[:,:,0]
        hist, b = np.histogram(hue, 256, (0, 256))
        new = patern_hue_hist[hue]
        #out = hist[hue]


        x1 = 100
        y1 = 100
        x2 = x1+x
        y2 = y1+y
        cv2.rectangle(bgr, (x1, y1), (x2, y2), (0, 255, 0))
        cv2.imshow('Image', new)
        #cv2.imshow('Image', bgr)

        
        # Wait for key
        key = 0xFF & cv2.waitKey(30)
        if key == 27:
            break
        
    cv2.destroyAllWindows()
    print("Done")

# END
