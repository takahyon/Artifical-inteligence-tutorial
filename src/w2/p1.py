import numpy as np
import matplotlib.pyplot as plt


def img_prepare(file_name):
    """
    画像の前処理関数
    :param file_name:
    :return numpy array
    """
    img = plt.imread(file_name)
    # remove alpha
    if len(img[0, 0]) > 3:
        img = img[:, :, :3]
    # convert to float
    if img.dtype != float:
        img = img / 255
    # grayscale
    if len(img.shape) > 2:
        img = img.mean(axis=2)

    return img


def get_info(img):
    """
    画像を情報込みの画像を表示
    :param img:
    :return numpy array
    """
    plt.imshow(img, cmap="gray")
    print("Image Width" + str(img.shape[0]))
    print("Image Height" + str(img.shape[1]))
    print("Image Brighter" + str(np.max(img)))
    print("Image Darker" + str(np.min(img)))


def img_filp_v(img):
    """
    画像を上下左右体格に反転
    :param img:
    :return numpy array
    """

    return img[::-1]


def img_filp_h(img):
    """
    画像を上下左右体格に反転
    :param img:
    :return numpy array
    """

    return img[:, ::-1]


def img_filp_t(img):
    """
    画像を上下左右体格に反転
    :param img:
    :return numpy array
    """

    return img.T


def img_rotate(img, angle):
    """
    画像を上下左右体格に反転
    :param img:
    :param angle: 回転角度

    :return numpy array
    """
    res = img
    if angle > 0:
        for i in range(int(angle / 90)):
            res = res[::-1].T
    else:
        print("input nature numbers")

    return res

def img_small(img, multipul):
    """
    画像を縮小
    :param img:
    :param multipul: 倍率の分母

    :return numpy array
    """

    res = img[::multipul, ::multipul]

    return res


def binarize(img, thres):
    """
    画像を2ちか
    :param img:
    :param thres: 閾値

    :return numpy array
    """

    res = img > thres
    res.astype(int)

    return res


def img_filter(img, algorithm, laps_hard=True):
    """
    画像をフィルタにかけるよ
    :param img:
    :param thres: 閾値

    :return numpy array
    """
    al = algorithm

    filt = np.ones(9).reshape(3, 3)

    # ガウシアンフィルタ
    if al == "g":
        filt = np.ones(9).reshape(3, 3) / 16
        filt[1] *= 2
        filt[:, 1] *= 2
    # そーベルフィルタ
    elif al == "s":
        filt = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    # らぷシアンフィルタ
    elif al == "l":
        filt = np.ones(9).reshape((3, 3))
        laps = 0
        if laps_hard:
            laps = -8
        else:
            laps = -4
        filt[1,1] *= laps
        print(filt)

    # 実際にかける
    h, w = img.shape

    after = np.zeros_like(img)

    for i in range(h - 2):
        for j in range(w - 2):
            after[i, j] = (img[i:i + 3, j:j + 3] * filt).sum()

    plt.imshow(after, cmap="gray")
    return after


# def face_detect(img):
#     import cv2
#     model = cv2.CascadeClassifier(path)
#     plt.imshow(img[a:a + h, b:b + w])
img = img_prepare('lena_color.gif')
