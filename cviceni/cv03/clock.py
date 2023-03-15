# By Pytel

"""
Program pro simulaci ručičkových hodin.
"""

from PIL import Image
import PIL
import numpy as np
import cv2
import os
from datetime import datetime, timedelta
import time

clock_folder = "watch_face/"
clock_face = "cronometer.png"
clock_dot = "cronometer_dot.png"
clock_h = "cronometer_h.png"
clock_m = "cronometer_m.png"
clock_s = "cronometer_s.png" 

class Clock:
    def __init__(self, clock_face, clock_dot, hands):
        self.face = Image.open(clock_face)
        self.dot = enlarge_canvas_and_center(Image.open(clock_dot), self.face.size)
        self.hands = []
        for hand in hands:
            hand = Image.open(hand)
            hand_large = enlarge_canvas_and_center(hand, self.face.size)
            self.hands.append(hand_large)

    def _clock_time_to_angle(self, time: tuple()) -> tuple():
        """ Convert time to angle
        """
        h, m, s = time
        h = h % 12
        h_angle = (h * 30) + (m / 2) + (s / 120)
        m_angle = (m * 6) + (s / 10)
        s_angle = s * 6
        return (h_angle, m_angle, s_angle)

    def generate_clock(self, time: tuple()) -> Image:
        # convert time to angle
        angle = self._clock_time_to_angle(time)

        # rotate hands
        hands_rotated = []
        for i in range(len(self.hands)):
            hands_rotated.append(self.hands[i].rotate(-angle[i], PIL.Image.NEAREST))

        # create clock
        clock = Image.new("RGBA", self.face.size)
        clock = Image.alpha_composite(clock, self.face)
        for hand in hands_rotated:
            clock.alpha_composite(hand)
        clock = Image.alpha_composite(clock, self.dot)
        return clock
    
    def show_assets(self):
        self.face.show()
        self.dot.show()
        for hand in self.hands:
            hand.show()

def enlarge_canvas_and_center(pic : Image, dimensions : tuple) -> Image:
    large = Image.new('RGBA', dimensions)
    center = (
        int(large.size[0]/2) - int(pic.size[0]/2),
        int(large.size[1]/2) - int(pic.size[1]/2)
    )
    large.paste(pic, center)
    return large

def demo():
    # hands
    hands = [clock_folder + clock_h, clock_folder + clock_m, clock_folder + clock_s]
    
    # get time
    date_time = datetime.now()
    clock = Clock(clock_folder + clock_face, clock_folder + clock_dot, hands)
    while True:
        # get time
        date_time = date_time + timedelta(seconds=1)
        clock_time = [date_time.hour, date_time.minute, date_time.second]
        rgb = cv2.cvtColor(np.array(clock.generate_clock(clock_time)), cv2.COLOR_BGR2RGB)
        cv2.imshow('Image', rgb)

        # Wait for key
        key = 0xFF & cv2.waitKey(30)
        if key == 27:
            break
        #time.sleep(0.01)
    
    cv2.destroyAllWindows()

def show_time():
    # hands
    hands = [clock_folder + clock_h, clock_folder + clock_m, clock_folder + clock_s]
    
    # get time
    date_time = datetime.now()
    clock = Clock(clock_folder + clock_face, clock_folder + clock_dot, hands)
    clock_time = [date_time.hour, date_time.minute, date_time.second]
    clock.generate_clock(clock_time).show()


if __name__ == "__main__":
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    elif os.name == 'posix':
        clear = lambda: os.system('clear')
    clear()

    #show_time()
    demo()
    print("Done")
    
