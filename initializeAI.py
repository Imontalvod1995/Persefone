#####################################################
#                 initializeAI.py                   #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# Initialization of the Artificial Inteligence.     #
# Here, given a descriptor-extractor (SIFT) and a   #
# distribution in space (via K-Means), we train a   #
# system with our train data.                       #
#                                                   #
#####################################################

import glob
import os

import cv2 as cv
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.neural_network import MLPClassifier

import dictTranslate as dicT

def initialize(sift):

    pthTrain = 'trainData/'
    charLimit = len(pthTrain)
    previousChar = '0T'
    label = 0
    DL = []
    LB = []
    listOfHist = []

    for filename in glob.glob(os.path.join(pthTrain, '*.tif')):

        currentChar = filename.split('_')[0][charLimit:]
        img = cv.imread(filename)
        kp, des = sift.detectAndCompute(img, None)

        if np.shape(des) == ():
            continue
        else:
            for d in des:
                DL.append(d)

        if currentChar == previousChar:
            LB.append(label)
        else:
            previousChar = currentChar
            label += 1
            LB.append(label)

    DL = np.array(DL)
    LB = np.array(LB)[..., np.newaxis]

    ##############
    # CLUSTERING #
    ##############

    k = 430
    batch_size = np.size(os.listdir(pthTrain)) * 3

    kmeans = MiniBatchKMeans(n_clusters=k, batch_size=batch_size, verbose=1).fit(DL)

    ##############
    # HISTOGRAMS #
    ##############

    kmeans.verbose = False

    for filename in glob.glob(os.path.join(pthTrain, '*.tif')):
        img = cv.imread(filename)
        kp, des = sift.detectAndCompute(img, None)

        hist = np.zeros(k)
        nk = np.size(kp)

        if np.shape(des) == ():
            continue
        else:
            for d in des:
                idv = kmeans.predict([d])
                hist[idv] += 1 / nk

            listOfHist.append(hist)

    X = np.array(listOfHist)
    Y = LB

    mlp = MLPClassifier(verbose=True, max_iter=600000)
    mlp.fit(X, Y)

    return k, kmeans, mlp


def desiredValues(values, valset):
    # Prediction of the given character
    # with the system
    charList = []
    limit = -1 * valset
    sortedValues = sorted(values, key=float)

    for i in range(valset):
        currentVal = valset - (i + 1)
        charVal = sortedValues[limit:][currentVal][0]
        realChar = dicT.numberToLabel(np.where(values == charVal)[0][0])
        charList.append(realChar)

    return charList
