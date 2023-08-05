from matplotlib import pyplot as plt


def plt_show(image, title: str):
    plt.subplot(1, 1, 1), plt.imshow(image, 'gray')
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.show()
