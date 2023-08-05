import json

import cv2 as cv

from image2text.util.plt import plt_show
from image2text.util.image import default_image

data_width = 512
data_height = 512


def data_save(trimed):
    with open('x_data.json') as f:
        data_x: list = json.load(f)
    with open('y_data.json') as f:
        data_y: list = json.load(f)

    for index, i in enumerate(trimed):
        w = len(i[0])
        h = len(i)
        if w > h:
            zoom_rate = data_width / w
        else:
            zoom_rate = data_height / h

        tmp_ = cv.resize(i, (int(w * zoom_rate), int(h * zoom_rate)))
        tmp = default_image(data_width, data_height)
        for a, width in enumerate(tmp_):
            for b, pixel in enumerate(width):
                tmp[a][b] = int(pixel)

        plt_show(i, str(index))

        data_x.append([tmp])
        data_y.append(int(input(str(index) + "번째 값이 글씨인가 아닌가")))

    with open('x_data.json', 'w') as outfile:
        json.dump(data_x, outfile)
    with open('y_data.json', 'w') as outfile:
        json.dump(data_y, outfile)
