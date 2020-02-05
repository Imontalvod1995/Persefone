#####################################################
#               thresholdFuntions.py                #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# The idea behind this definition is to do a        #
# threshold given a limit. The idea is to           #
# binarize the image and reduce the noise.          #
#                                                   #
#####################################################

import cv2 as cv
import numpy as np


def thresh(img):
    # Here we want to do an adaptative threshold.
    # The idea of this threshold is to clean the
    # noise and let the image in a binary format.
    #
    # The input of this function is the paragraph
    # that we want to analyze.
    tLimit = 120

    medianBlur = cv.medianBlur(img, 5)
    th1 = cv.adaptiveThreshold(medianBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                               cv.THRESH_BINARY, 11, 2)

    gaussianBlur = cv.GaussianBlur(img, (3, 3), -1)
    _, th2 = cv.threshold(gaussianBlur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    total = th1 + th2

    total[total < tLimit] = 0
    total[total > tLimit] = 255

    tt = total.copy()
    tt[tt > tLimit] = 1

    kernel = np.ones((2, 2))
    cl2 = cv.morphologyEx(tt, cv.MORPH_CLOSE, kernel)
    op2 = cv.morphologyEx(cl2, cv.MORPH_OPEN, kernel)

    return op2
