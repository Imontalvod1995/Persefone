#####################################################
#                      GUI.py                       #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# Here the GUI is implemented to found the points   #
# of the paragraph that's going to be analyzed.     #
#                                                   #
#####################################################

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import cv2 as cv
import numpy as np
from PIL import Image, ImageTk

import main as mn
## Function Import
import startupFunctions as sF

holdFinal = []
clickCounter = 0
lines = 0
lineP = 0
points = np.zeros((4, 2))


def doneSelection():
    messagebox.showinfo('Selection', 'Four points have been selected')


def getFileName():
    return filedialog.askopenfilename(initialdir='/', title='Load Page',
                                      filetypes=(("TIF Files", "*.tif"), ("all files", "*.*")))


def on_click(event=None):
    global clickCounter, holdFinal
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    text = '({0},{1})'.format(int(x), int(y))
    holdFinal.append(text)
    clickCounter = clickCounter + 1
    if clickCounter == 4:
        doneSelection()
        root.destroy()


def distanceBetween(point):
    A = point[0]
    B = point[1]
    C = point[2]
    D = point[3]

    H = max(np.int(norm(A, B)), np.int(norm(C, D)))
    W = max(np.int(norm(B, C)), np.int(norm(A, D)))

    return H, W


def norm(X, Y):
    x_1, y_1 = X
    x_2, y_2 = Y

    return np.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def imgSection(H, W):
    fix = np.float32(np.array([[0, 0],  # Superior Izquierda
                               [0, H],  # Inferior Izquierda
                               [W, H],  # Superior Derecha
                               [W, 0]]))  # Inferior Derecha
    return fix


## IMAGE ADQUISITION
root = tk.Tk()
root.title('Perséfone - File Search')
root.geometry('1300x500')

strg = getFileName()

frame = Frame(root, bd=2, width=1300, height=500)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E + W)

yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N + S)

canvas = Canvas(frame, width=1300, height=500)
canvas.grid(row=0, column=0, sticky=N + S + E + W)

img = ImageTk.PhotoImage(Image.open(strg))
canvas.create_image(0, 0, image=img, anchor="nw")

canvas.bind('<Button-1>', on_click)

yscroll.config(command=canvas.yview)
xscroll.config(command=canvas.xview)
canvas.config(scrollregion=canvas.bbox(ALL))

frame.pack()
root.mainloop()

## PARAGRAPH POINTS ADQUISITION AND PERSPECTIVE
for i in range(4):
    points[i, 0] = holdFinal[i][1:-1].split(',')[0]
    points[i, 1] = holdFinal[i][1:-1].split(',')[1]

points = np.float32(points)
h, w = distanceBetween(points)
sec = imgSection(h, w)

imh = cv.imread(strg, -1)[:, :, 0]
M = cv.getPerspectiveTransform(points, sec)
dst = cv.warpPerspective(imh, M, (w, h))

## PARAGRAPH PROCESS
lineP = input("Number of Lines: ")
lines = int(lineP)
mn.calcChar(dst, lines)
sF.removeInnerFolders('Character/')
