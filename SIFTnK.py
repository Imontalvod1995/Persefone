#####################################################
#                    SIFTnK.py                      #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# Recopilation and saving process of the analyzed   #
# characters. We give a total of 5 possibilities    #
# for each character.                               #
#                                                   #
#####################################################

import glob
import os

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import seed

import initializeAI as iAI
import startupFunctions as sF

seed(420)


def saveResults(charFile, charTitle, charVal):
    plt.imshow(charFile)
    plt.title(str(charTitle))
    plt.axis('off')

    plt.savefig('Results/' + str(charVal) + '.png')


sF.createFolder('Results')
sF.remove_contents('Results')

sift = cv.xfeatures2d.SIFT_create()
k, kmean, mlp = iAI.initialize(sift)

counter = 1
amountOfWords = len(os.listdir('Word/'))
pthChar = 'Character/'

for i in range(amountOfWords):
    currentFolder = pthChar + 'Word_' + str(i + 1)
    folderSize = len(currentFolder) + 1
    for filename in glob.glob(os.path.join(currentFolder, '*.tif')):
        if folderSize == 0:
            continue
        else:
            currentChar = filename[folderSize:]
            img = cv.imread(filename)
            kpTest, desTest = sift.detectAndCompute(img, None)
            row = []
            probChar = []

            xTest = np.zeros(k)
            nkpTest = np.size(kpTest)

            if np.shape(desTest) == ():
                row.append(currentFolder)
                row.append(currentChar)
                row.append('_')
            else:
                for d in desTest:
                    idTest = kmean.predict([d])
                    xTest[idTest] += 1 / nkpTest

                res = mlp.predict_proba([xTest])

                values = np.transpose(res)
                probChar = iAI.desiredValues(values, 5)

                saveResults(img, probChar, counter)
                counter += 1
