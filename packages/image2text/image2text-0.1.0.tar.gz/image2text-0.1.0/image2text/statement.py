from image2text.analysis.statement import image_prepare_BGR, image_prepare_path
from image2text.analysis.general import read_text
from skimage import io


def path_to_full_text(image_path, lang, mode='-c preserve_interword_spaces=1 --psm 6', minLineLength=80,
                      maxLineGap=5, printMode=False):
    data = image_prepare_path(image_path, minLineLength=minLineLength, maxLineGap=maxLineGap)
    data.reverse()
    return '\n'.join(read_text(data, mode, lang, printMode=printMode))


def url_to_full_text(url, lang, mode='-c preserve_interword_spaces=1 --psm 6', minLineLength=80,
                     maxLineGap=5, printMode=False):
    image = io.imread(url)
    data = image_prepare_BGR(image, minLineLength=minLineLength, maxLineGap=maxLineGap)
    data.reverse()
    return '\n'.join(read_text(data, mode, lang, printMode=printMode))
