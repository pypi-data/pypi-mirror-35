import numpy as np
import sys
import cv2 as cv

minLineLength = 80
maxLineGap = 5


def default_image(w, h):
    tmp = list()
    for i in range(h):
        tmp_inside = list()
        for j in range(w):
            tmp_inside.append(0)
        tmp.append(tmp_inside)
    return tmp


def get_image_path():
    if len(sys.argv) == 1:
        exit()
    return sys.argv[1]

