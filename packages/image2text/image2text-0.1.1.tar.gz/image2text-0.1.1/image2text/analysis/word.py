import numpy as np
import cv2 as cv


def image_prepare(image_path: str, output=None, minLineLength=80, maxLineGap=5):
    image = cv.imread(image_path)

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    kernel = np.ones((2, 2), np.uint8)

    gradient = cv.morphologyEx(image_gray, cv.MORPH_GRADIENT, kernel)

    th2 = cv.adaptiveThreshold(gradient, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 12)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv.morphologyEx(th2, cv.MORPH_CLOSE, kernel)

    lines = cv.HoughLinesP(closing, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    if lines is not None:
        for i in range(len(lines)):
            for x1, y1, x2, y2 in lines[i]:
                if abs(y1 - y2) > len(closing) / 7:
                    cv.line(closing, (x1, y1), (x2, y2), (0, 0, 0), 10)

    _, contours, _ = cv.findContours(closing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    tmp = list()
    tmp2 = list()
    for index, i in enumerate(contours):
        x, y, w, h = cv.boundingRect(i)
        if h > 5 and w > 5 and not (w >= len(image[0]) - 5 and h >= len(image) - 5):
            tmp2.append((x, y, w, h))
            tmp.append(gradient[y:y + h, x:x + w])

    if output == 'raw_image':
        for index, i in enumerate(contours):
            x, y, w, h = cv.boundingRect(i)
            if h > 5 and w > 5 and not (w >= len(image[0]) - 5 and h >= len(image) - 5):
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv.imwrite(image_path.replace('input', 'output'), image)
    if output == 'gradient_image':
        cv.imwrite(image_path.replace('input', 'output'), gradient)

    return tmp, tmp2


def add_space(data, trimed_place):
    result: str = ''

    for index in range(len(data) - 1):

        x, y, w, h = trimed_place[index]
        n_x, n_y, n_w, n_h = trimed_place[index + 1]
        if abs(n_x - w - x) < h / 2:
            if abs(n_y - h - y) < h / 2:
                result += data[index]
            else:
                result += data[index] + ' '
        else:
            if 2 * h > abs(n_y - h - y) > h / 2:
                result += data[index]
            else:
                result += data[index] + '\n'
    result += data[len(data) - 1]
    return result
