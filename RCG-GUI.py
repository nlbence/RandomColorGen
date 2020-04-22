import os
import time
import random
import pathlib
import tkinter as tk
import keyboard as kb
import pyperclip as clipboard
from tkinter import filedialog
from tkinter import messagebox

hasSaved = bool(False)
rgbFull = str()
hexFull = str()
customPath = str(None)
hexBG = str()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

root.title('Random Color Generator')
root.geometry('300x270')
root.resizable(0,0)

def randomRGB():
    global hasSaved
    global hexFull
    global hexBG
    global rgbFull
    global textColor
    hasSaved = False

    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))

    rHEX = hex(r)[2:]
    gHEX = hex(g)[2:]
    bHEX = hex(b)[2:]

    rBG = str(hex(int(r / 3)))[2:]
    gBG = str(hex(int(g / 3)))[2:]
    bBG = str(hex(int(b / 3)))[2:]

    grayscale = int((r + g + b) / 3)
    if grayscale <= 100:
        textColor = '#FFFFFF'
    elif 200 > grayscale > 100 == True:
        textColor = '#404040'
    else:
        textColor = '#000000'

    if len(rBG) == 1:
        rBG = '0' + rBG
    if len(gBG) == 1:
        gBG = '0' + gBG
    if len(bBG) == 1:
        bBG = '0' + bBG

    if len(rHEX) == 1:
        rHEX = '0' + rHEX
    if len(gHEX) == 1:
        gHEX = '0' + gHEX
    if len(bHEX) == 1:
        bHEX = '0' + bHEX

    hexBG = f'#{rBG}{gBG}{bBG}'
    rgbFull = f'{r}, {g}, {b}'
    hexFull = f'#{rHEX}{gHEX}{bHEX}'

    return hexFull, hexBG, textColor, rgbFull

def copyToClipboard(copyWhat: str):
    if copyWhat == 'RGB':
        clipboard.copy(rgbFull)
    elif copyWhat == 'HEX':
        clipboard.copy(hexFull)


def saveToTXT():
    global hasSaved
    hasSaved = True
    if customPath == None:
        currentTime = time.strftime("%H-%M-%S")
        date = time.strftime("%d-%m-%Y")
        pathToScript = pathlib.Path(__file__).parent.absolute()
        pathCustom = f'SavedColors\\{date}'
        fileName = f'{currentTime}.txt'
        pathFull = os.path.join(pathToScript, pathCustom)
        pathFullExt = os.path.join(pathFull, fileName)
        try:
            os.makedirs(pathFull)
        except:
            pass
    else:
        pathFullExt = customPath

    f = open(pathFullExt, 'w+')
    f.write(f'RGB: {rgbFull}\n')
    f.write(f'HEX: #{hexFull}')
    f.close()

def changeSavePath():
    global customPath
    customPath = filedialog.asksaveasfilename()
    return customPath

def on_closing():
    if kb.is_pressed('shift' or 'lshift'):
        root.destroy()
    else:
        if hasSaved == False:
            if messagebox.askokcancel("Quit", "Are you sure you want to quit without saving the color?"):
                root.destroy()


def newColor():
    randomRGB()
    root.configure(bg = hexBG)
    buttRegen.configure(fg = textColor, bg = hexFull)
    #root.update()

if __name__ == '__main__':  

    randomRGB()

    root.configure(bg = hexBG)

    buttRegen =  tk.Button(frame,
                         text = 'New Color',
                         fg = textColor,
                         bg = hexFull,
                         command = newColor)

    buttRegen.grid(row = 1, column = 2)

    root.protocol('WM_DELETE_WINDOW', on_closing)

    root.mainloop()