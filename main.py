#####################################################
#                      main.py                      #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# Here we do the whole character adquisition        #
# process.                                          #
#                                                   #
#####################################################

import os

import cv2 as cv
import numpy as np

import charFunctions as cF
import lineFunctions as lF
## Function Import
import startupFunctions as sF
import thresholdFunctions as tF
import wordFunctions as wF


def calcChar(im_inicial, lines):
    ## Cleaning and Creation of folders
    sF.startFolders()
    sF.remove_contents('Lines')
    sF.remove_contents('Word')
    sF.remove_contents('Rotation')
    sF.remove_contents('Section')
    sF.remove_contents('Character')

    ## PROCESS

    # Threshold to the given paragraph
    img = tF.thresh(im_inicial)

    # Creation of lines inside the paragraph
    _ = lF.lineExport(img, lines)

    # Start of separation of words inside a line
    numberOfLines = len(os.listdir('Lines'))

    for i in range(numberOfLines):
        # Current Line inside the folder
        currentLine = 'Lines/L_' + str(i + 1) + '.tif'
        linea = cv.imread(currentLine, -1)
        U, _ = np.shape(linea)

        # Save words found inside the line
        wide, close = wF.wide_close_range(0, U)
        nClose, nWide = wF.N(wide, close, linea)
        interClose = wF.inter(nClose)
        interWide = wF.inter(nWide)
        sepClose = wF.f_val(interClose, close, linea)
        sepWide = wF.f_val(interWide, wide, linea)
        result = wF.specWord(sepWide, sepClose)
        wF.wordWrite(result, linea)

    # Process of Character Separation
    numberOfWords = len(os.listdir('Word'))

    # Rotation of each word
    for i in range(numberOfWords):
        strL = 'Word/Word_' + str(i + 1) + '.tif'
        cv.imwrite(os.path.join('Rotation', 'Rot_' + str(i + 1) + '.tif'), cF.newRotation(strL))

    sF.remove_contents('Character/')

    # Extraction of character given rotated word      
    for i in range(len(os.listdir('Rotation/'))):
        currentIteration = i + 1
        strHT = 'Rotation/Rot_' + str(currentIteration) + '.tif'
        cF.sectionMgmt(strHT, 'Section')
        sF.createFolder('Character/Word_' + str(currentIteration) + '/')
        cF.characterSet(currentIteration)

    print('Separation of characters done!')
## END
