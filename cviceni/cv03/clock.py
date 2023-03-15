# By Pytel

"""
Program pro simulaci ručičkových hodin.
"""

from PIL import Image
import PIL
import cv2
import os

clock_folder = "watch_face/"
clock_face = "cronometer.png"
clock_dot = "cronometer_dot.png"
clock_h = "cronometer_h.png"
clock_m = "cronometer_m.png"
clock_s = "cronometer_s.png" 


if __name__ == "__main__":
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    elif os.name == 'posix':
        clear = lambda: os.system('clear')
    clear()

    # load images
    clock_face = cv2.imread(clock_folder + clock_face)
    clock_dot = cv2.imread(clock_folder + clock_dot)
    clock_h = cv2.imread(clock_folder + clock_h)
    clock_m = cv2.imread(clock_folder + clock_m)
    clock_s = cv2.imread(clock_folder + clock_s)

    # create clock
    
    clock_face = Image.open(clock_folder + clock_face)
    clock_s = Image.open(clock_folder + clock_s)
    clock_s_rotated = clock_s.rotate(43, PIL.Image.NEAREST)
    
    clock = Image.new("RGBA", clock_face.size)
    clock = Image.alpha_composite(clock, clock_face)
    clock = Image.alpha_composite(clock, clock_s_rotated)

    clock.show()

    #cv2.imshow('Time', clock_s_rotated)
    cv2.imshow('Time', clock)
    cv2.waitKey(0)

