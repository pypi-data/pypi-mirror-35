import cv2 as cv
import numpy as np


def image_prepare_path(image_path: str, minLineLength=80, maxLineGap=5):
    image = cv.imread(image_path)

    tmp, contours = image_prepare_BGR(image, minLineLength, maxLineGap)

    return tmp


def image_prepare_BGR(image_BGR: str, minLineLength=80, maxLineGap=5):
    image_gray = cv.cvtColor(image_BGR, cv.COLOR_BGR2GRAY)

    kernel = np.ones((2, 2), np.uint8)
    gradient = cv.morphologyEx(image_gray, cv.MORPH_GRADIENT, kernel)

    th2 = cv.adaptiveThreshold(gradient, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 12)
    kernel = np.ones((17, 25), np.uint8)
    closing = cv.morphologyEx(th2, cv.MORPH_CLOSE, kernel)

    lines = cv.HoughLinesP(closing, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    if lines is not None:
        for i in range(len(lines)):
            for x1, y1, x2, y2 in lines[i]:
                if abs(y1 - y2) > len(closing) / 7:
                    cv.line(closing, (x1, y1), (x2, y2), (0, 0, 0), 10)

    _, contours, _ = cv.findContours(closing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    tmp = list()
    for index, i in enumerate(contours):
        x, y, w, h = cv.boundingRect(i)
        if h > len(image_BGR) / 30 and w > len(image_BGR[0]) / 7 and not (
                w >= len(image_BGR[0]) - 5 and h >= len(image_BGR) - 5):
            tmp.append(image_BGR[y:y + h, x:x + w])

    return tmp
