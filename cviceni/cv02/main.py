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
from camshift import *

pattern_file = "cv02_vzor_hrnecek.bmp"
video_file = "cv02_hrnecek.mp4"


def process_image(image):
    """ Process image
    """
    bgr = cv2.imread(image)

    # Plot
    plt.figure()
    plt.subplot(1, 3, 1)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)

    plt.subplot(1, 3, 2)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    plt.imshow(hsv)

    plt.subplot(1, 3, 3)
    hist = img2hue_histogram(bgr)
    plt.plot(hist)
    plt.title("Histogram")
    plt.xlabel("Hue")
    plt.ylabel("Count")

    plt.show()

    # picure size
    print("Image size: {0}".format(rgb.shape))

    plt.waitforbuttonpress()


if __name__ == "__main__":
    plt.ion()
    #clear = lambda: os.system('cls')
    def clear(): return os.system('clear')
    clear()
    plt.close('all')

    # process_image(pattern_file)
    # exit()

    camshift = CamShift(pattern_file)

    cap = cv2.VideoCapture(video_file)
    while True:
        ret, bgr = cap.read()
        if not ret:
            break

        (x1, y1), (x2, y2) = camshift.next_positon(bgr)

        cv2.rectangle(bgr, (x1, y1), (x2, y2), (0, 255, 0))
        cv2.imshow('Image', bgr)

        """
        patern_bgr = cv2.imread(pattern_file)
        pattern_hue_hist = img2hue_histogram(patern_bgr)
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        hue = hsv[:,:,0]

        # img projection
        hue_projection = pattern_hue_hist[hue]
        cv2.rectangle(hue_projection, (x1, y1), (x2, y2), (255, 255, 255))
        cv2.imshow('Image', hue_projection)
        """

        # Wait for key
        key = 0xFF & cv2.waitKey(30)
        if key == 27:
            break

    cv2.destroyAllWindows()
    print("Done")

# END
