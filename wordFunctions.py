#####################################################
#                  wordFuntions.py                  #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# The idea behind this definitions is to separate   #
# the word inside the given line.                   #
# To do this, we make two groups of lines: a whole  #
# line split and a inner section line split. This   #
# splits are composed by five lines who cut a       #
# section evenly. Given this, we do an intersection #
# between the whites of all of these lines. This    #
# will be lines that come across the whole line and #
# potential word-splitters.                         #
#                                                   #
#####################################################

import os

import cv2 as cv
import numpy as np


def wide_close_range(lim_down, lim_up):
    # Creation of the lines for both
    # wide and close analysis.
    # The wide one divides the whole line
    # meanwhile, the close one divides
    # the inner section.
    wd_val = (lim_up - lim_down) // 6
    wide = []
    close = []
    for i in range(5):
        wide.append((i + 1) * wd_val)
    cl_val = (wide[3] - wide[1]) // 6
    for j in range(5):
        close.append(wide[1] + (j * cl_val))

    return wide, close


def N(wide, close, linea):
    ## N is defined through the values of wide and close.
    ## Then N[0] for any of them is linked to wide[0] or close[0]
    N_wide = []
    N_close = []

    assert len(wide) == len(close)

    for i in range(len(wide)):
        N_wide.append(np.where(linea[wide[i]] == 1))
        N_close.append(np.where(linea[close[i]] == 1))
    return N_close, N_wide


def inter(N):
    # Intersections between the white-found arrays.
    inter_1 = np.intersect1d(N[0], N[1])
    inter_2 = np.intersect1d(N[2], N[3])
    inter_3 = np.intersect1d(inter_1, inter_2)
    inter_fin = np.intersect1d(inter_3, N[4])

    return inter_fin


def f_val(inter, analysis, linea):
    # Given the type of analysis, the given
    # values for word separation are determined.

    valores = []
    compv = []
    sep_linea_1 = []
    sep_linea_2 = []
    val_2 = []
    val_3 = []

    for i in range(len(inter) - 1):
        a = inter[i]
        b = inter[i + 1]
        compv.append(a)
        if b - a != 1:
            if len(compv) > 1:
                valores.append(a)
            compv = []

    val = np.array(valores)

    for j in range(len(val)):
        if np.sum(linea[:, val[j]]) >= np.shape(linea)[0]:
            sep_linea_1.append(val[j])
        else:
            val_2.append(val[j])

    for k in range(len(val_2)):
        if np.sum(linea[analysis[1]:analysis[3], val_2[k]]) >= (analysis[3] - analysis[1]):
            sep_linea_2.append(val_2[k])
        else:
            val_3.append(val_2[k])

    sep = sep_linea_1 + sep_linea_2
    sep.sort()

    return sep


def specWord(sep_w, sep_c):
    # We cross and compare the results between both 
    # types of analysis to give a consolidated
    # section array.
    sep_total = sep_w + sep_c
    sep_total.sort()

    alf = sep_total.copy()

    for x in range(len(sep_total) - 1):
        dif = sep_total[x + 1] - sep_total[x]
        if dif < 13:
            alf[x + 1] = alf[x]

    final_alf = list(set(alf))
    final_alf.sort()

    for y in range(len(final_alf) - 1):
        nd = final_alf[y + 1] - final_alf[y]
        if nd <= 15:
            final_alf[y] = final_alf[y + 1]

    result = list(set(final_alf))
    result.sort()

    return result


def wordWrite(result, linea):
    # With some restrictions, write the word-elements that
    # were detected
    if not len(os.listdir('Word/')):
        count = 1
    else:
        count = len(os.listdir('Word/')) + 1
    for h in range(len(result) - 1):
        coor_x1 = result[h]
        coor_x2 = result[h + 1]
        im_seg = linea[:, coor_x1:coor_x2]
        cv.imwrite(os.path.join('Word', 'Word_' + str(count) + '.tif'), im_seg)
        count = count + 1

## END
