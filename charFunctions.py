#####################################################
#                  charFuntions.py                  #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# The idea behind this definitions is to separate   #
# the characters inside a word using a rotation due #
# to inclination of the words.                      #
#                                                   #
#####################################################

import os

import cv2 as cv
import numpy as np

import startupFunctions as sF


def newRotation(strg):
    # Make a rotation, given by the inclination
    # of the word.
    # There're some restrictions of the long words
    # because the angle between the principal components
    # is so small or just too big. 
    dst = 0
    pos = []
    t = cv.imread(strg, -1)

    t[t == 1] = 255
    t[t == 0] = 1
    t[t == 255] = 0

    X, Y = np.shape(t)
    whole_test = np.zeros((X * 2, Y * 3))
    X_1, Y_1 = np.shape(whole_test)
    whole_test[X // 2:3 * X // 2, Y // 2:3 * Y // 2] = t

    for i in range(X_1):
        for j in range(Y_1):
            if whole_test[i, j] == 1:
                pos.append([np.abs(i - Y_1), j])

    data = np.array(pos)
    cvm = np.cov(data.T)
    _, eVec = cv.eigen(cvm)[1:]

    [m1, m2] = eVec[0]
    angle = np.int(np.abs(np.arctan(m1 / m2) * 180 // 3.1415))

    if angle < 15:
        angle = 15
    elif angle > 25:
        angle = 25

    rot_mat = cv.getRotationMatrix2D((X // 2, Y // 2), angle, 1)

    dst = cv.warpAffine(t, rot_mat, (Y_1, X_1))
    dst[dst == 1] = 255
    dst[dst == 0] = 1
    dst[dst == 255] = 0
    dst.reshape(Y_1, X_1)

    kernel = np.ones((2, 2))
    cl2 = cv.morphologyEx(dst, cv.MORPH_CLOSE, kernel)
    op2 = cv.morphologyEx(cl2, cv.MORPH_OPEN, kernel)

    return op2


def holdSep(img, sumV, sumR):
    # Determination of the up and down
    # limits of the image.
    h = []
    vLim = [0]
    hLim = [0]

    I, J = np.shape(img)

    # Vertical Limits
    for i in range(I):
        if sumV[I - i - 1] == J:
            h.append(I - i)

    h.append(0)

    for j in range(len(h) - 1):
        if h[j] - h[j + 1] == 1:
            continue
        else:
            vLim.append(h[j + 1])
            vLim.append(h[j])

    # Horizontal Limits
    h = []
    for l in range(J):
        if sumR[J - l - 1] == I:
            h.append(J - l)

    h.append(0)

    for k in range(len(h) - 1):
        if h[k] - h[k + 1] == 1:
            continue
        else:
            hLim.append(h[k + 1])
            hLim.append(h[k])

    return vLim, hLim


def wordLines(img):
    # Creation of the lines inside 
    # the word, following the same method
    # as the word separation to separate 
    # the characters.
    X, _ = np.shape(img)

    prim_lines = []
    prim_valW = X // 13

    for j in range(8):
        prim_lines.append((j + 1) * prim_valW)

    return prim_lines


def lineSet(img, w_line):
    # Searching the white and do the 
    # intersection to search the lines 
    # who split the word in characters

    # w_line[2] = w_line[2]+1
    # w_line[0] = w_line[0]+1
    # w_line[5] = w_line[5]+2
    # w_line[7] = w_line[7]-2

    a_1 = np.where(img[w_line[0] + 1] == 1)
    a_2 = np.where(img[w_line[1] - 1] == 1)
    a_3 = np.where(img[w_line[2]] == 1)
    a_4 = np.where(img[w_line[3] - 1] == 1)
    a_5 = np.where(img[w_line[4] + 2] == 1)
    a_6 = np.where(img[w_line[5]] == 1)
    a_7 = np.where(img[w_line[6]] == 1)
    a_8 = np.where(img[w_line[7] - 2] == 1)

    inter_1 = np.intersect1d(a_1, a_2)
    inter_2 = np.intersect1d(a_3, a_4)
    inter_3 = np.intersect1d(a_5, a_6)
    inter_4 = np.intersect1d(a_7, a_8)

    inter_a = np.intersect1d(inter_1, inter_3)
    inter_b = np.intersect1d(inter_2, inter_4)
    inter_c = np.intersect1d(inter_a, inter_b)

    return inter_c


def closedSpace(img):
    # Due to the image enlargement in the 
    # rotation process, this function cuts 
    # the image to only the character.
    im = img.copy()
    hts = []
    X, Y = np.shape(im)
    vSum = np.sum(im, axis=1)
    setVS = np.where(vSum == Y)[0]

    for x in range(len(setVS) - 1):
        a = setVS[x]
        b = setVS[x + 1]
        if b - a > 1:
            hts.append(a)
            hts.append(b)
    if hts == []:
        hts.append(0)
        hts.append(X)

    im = im[int(hts[0]):int(hts[1]), :]

    return im


def sectionMgmt(strR, strSelect):
    # Use of the other functions to find
    # sections in a word.
    Rot = cv.imread(strR, -1)

    sumR = np.sum(Rot, axis=0)
    sumV = np.sum(Rot, axis=1)

    hLim, vLim = holdSep(Rot, sumV, sumR)

    vLim.sort()
    hLim.sort()

    sF.remove_contents(strSelect)

    cnt = 0
    for x in range(len(vLim) - 1):
        for y in range(len(hLim) - 1):
            setimg = Rot[hLim[y]:hLim[y + 1], vLim[x]:vLim[x + 1]]
            S, T = np.shape(setimg)
            mean = np.int(np.sum(setimg))

            if mean == (S * T):
                continue
            else:
                if S >= 6 and T >= 7:
                    cnt = cnt + 1
                    cv.imwrite(os.path.join(strSelect, 'Sec_' + str(cnt) + '.tif'), closedSpace(setimg))


def characterSet(it):
    # Find the characters inside the sections
    ch = len(os.listdir('Section/'))

    for i in range(ch):
        count = 1

        li = [0]
        cm = []
        strH = 'Section/Sec_' + str(i + 1) + '.tif'
        sR = cv.imread(strH, -1)
        _, B = np.shape(sR)
        w_line = wordLines(sR)
        inter = lineSet(sR, w_line)

        for y in range(len(inter) - 1):
            a = inter[y]
            b = inter[y + 1]
            cm.append(b - a)
            if cm[y] > 3:
                li.append(inter[y])

        li.append(B)
        li = list(set(li))
        li.sort()

        for j in range(len(li)):
            if j + 1 >= len(li):
                continue
            else:
                a = li[j]
                b = li[j + 1]
                charWhole = sR[:, a:b]
                X, Y = np.shape(charWhole)
                mean = np.int(np.mean(charWhole))
                if mean == X * Y:
                    continue
                else:
                    if Y > 8:
                        if X >= 17:
                            print('Setting characters of word ' + str(it) + '.')
                            cv.imwrite(os.path.join('Character/Word_' + str(it) + '/', 'Ch_' + str(count) + '.tif'),
                                       charWhole * 255)
                            count = count + 1
## END
