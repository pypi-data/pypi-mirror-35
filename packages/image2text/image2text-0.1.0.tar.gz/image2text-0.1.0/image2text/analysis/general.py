import re

import pytesseract as pt


def word_compile(image, lang: str, mode: str, printMode=False):
    try:
        if lang == 'ko':
            kor = pt.image_to_string(image, 'kor', config=mode)
            hangul = pt.image_to_string(image, 'Hangul', config=mode)

            kor_test = re.findall('[가-힣]', kor)
            hangul_test = re.findall('[가-힣]', hangul)
            if len(kor_test) == 0 and len(hangul_test) == 0:
                if len(kor) > len(hangul):
                    tmp = kor
                else:
                    tmp = hangul
            else:
                if len(kor_test) > len(hangul_test):
                    tmp = kor
                else:
                    tmp = hangul

            if printMode:
                print(tmp, end='\n\n')

            return tmp
        if lang == 'en':
            eng = pt.image_to_string(image, 'eng', config=mode)

            eng_test = re.findall('[a-b]', eng)

            return eng

        if lang == 'jp':
            jpn = pt.image_to_string(image, 'jpn', config=mode)
            japanese = pt.image_to_string(image, 'Japanese', config=mode)
            jpn_test_kan = re.findall('[\u4E00-\u9FFF]+', jpn)
            jpn_test_hi = re.findall('[\u3040-\u309Fー]+', jpn)
            jpn_test_ka = re.findall('[\u30A0-\u30FF]+', jpn)
            japanese_test_kan = re.findall('[\u4E00-\u9FFF]+', japanese)
            japanese_test_hi = re.findall('[\u3040-\u309Fー]+', japanese)
            japanese_test_ka = re.findall('[\u30A0-\u30FF]+', japanese)
            jpn_score = len(jpn_test_hi) * 3 + len(jpn_test_ka) * 2 + len(jpn_test_kan)
            japanese_score = len(japanese_test_hi) * 3 + len(japanese_test_ka) * 2 + len(japanese_test_kan)

            if jpn_score > japanese_score:
                tmp = jpn
            else:
                tmp = japanese

            if printMode:
                print(tmp, end='\n\n')

            return tmp

    except pt.TesseractError as e:
        print(e)
    return ''


def read_text(trimed, mode, lang, printMode=False):
    result = list()

    for index, i in enumerate(trimed):
        result.append(word_compile(i, lang, mode, printMode=printMode))

    return result
