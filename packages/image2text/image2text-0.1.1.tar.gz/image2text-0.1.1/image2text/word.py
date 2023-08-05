from image2text.analysis.word import image_prepare, add_space
from image2text.analysis.general import read_text


def path_to_full_text(image_path, lang, mode='-c preserve_interword_spaces=1 --psm 6', output=None, minLineLength=80,
                      maxLineGap=5, printMode=False):
    data, data_place = image_prepare(image_path, output=output, minLineLength=minLineLength, maxLineGap=maxLineGap)
    data.reverse()
    data_place.reverse()
    return add_space(read_text(data, mode, lang, printMode=printMode), data_place)
