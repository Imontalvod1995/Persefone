#####################################################
#                  lineFuntions.py                  #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# The idea behind this definitions is to separate   #
# the lines inside the given paragraph.             #
#                                                   #
#####################################################

import os

import cv2 as cv
import numpy as np


def lineSet(img, lines):
    # Given the n-number of lines, we split a projection
    # of the paragraph into n-sections. Inside this 
    # sections we want to identify the points which have
    # the most amount of white. Then a line is given 
    # through this points, making the location of the
    # lines visible.
    min_values = []
    max_values = []

    im_lat = np.sum(img, axis=1)
    separation_value = np.shape(im_lat)[0] // lines

    for i in range(lines):
        min_detect = im_lat[i * separation_value:(i + 1) * separation_value]
        min_values.append((i * separation_value) + np.where(min_detect == min_detect.min())[0][0])

    for j in range(len(min_values) - 1):
        appValue = 0
        minLimit = min_values[j]
        maxLimit = min_values[j + 1]
        section = np.where(im_lat == im_lat[minLimit:maxLimit].max())[0]
        lenSec = len(section)
        if lenSec == 1:
            appValue = section[0]
        else:
            for l in range(lenSec):
                if section[l] >= minLimit and section[l] <= maxLimit:
                    appValue = section[l]
        max_values.append(appValue)

    return max_values


def lineExport(img, lines):
    # Given the lines coordinates, we split them into
    # n lines.
    X, _ = np.shape(img)

    lines = lineSet(img, lines)
    lines.append(0)
    lines.append(X)
    lines.sort()

    amount_of_lines = len(lines) - 1
    line_matrix = np.zeros((amount_of_lines, 2))

    for i in range(amount_of_lines):
        startLine = lines[i]
        endLine = lines[i + 1]
        line_exp = img[startLine:endLine]
        line_matrix[i, 0] = startLine
        line_matrix[i, 1] = endLine

        cv.imwrite(os.path.join('Lines', 'L_' + str(i + 1) + '.tif'), line_exp)

    return line_matrix
## END
