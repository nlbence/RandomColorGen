import random
import os
import pyperclip
import time
import pathlib
import binascii
import tkinter as tk

os.system('cls')

root = tk.Tk()

saveAliases = ['SAVE', 'S']
validPrompts = ['cRGB', 'cHEX', 'Q', 'C'] + saveAliases
#validPromptsHex = binascii.hexlify(bytearray(validPrompts))
copyPrompts = ['RGB', 'HEX', 'Q']

r = random.choice(range(0,255))
g = random.choice(range(0,255))
b = random.choice(range(0,255))

def rgbToHex(rgb: int):
    return '%02x' % rgb

rgbFinal = f'{r}, {g}, {b}'
rgbHex = f'{rgbToHex(r)}{rgbToHex(g)}{rgbToHex(b)}'

print(f'{rgbFinal}')
print(f'#{rgbHex}')

root.title('Color Preview')
root.geometry('300x270')
root.configure(bg = f'#{rgbHex}')

prompt = str()
hasSaved = False
firstRun = True

print('Close the window to continue')
root.mainloop()

while prompt != 'Q':

    if firstRun == True:
        print("\nType 'c' to copy,\nType 'save' to save the color to a file\nor type 'q' to quit!")
        firstRun = False

    prompt = input('')
    prompt = str(prompt)
    prompt = prompt.upper()
    
    if prompt not in validPrompts:
        print('Not a valid option!')

    #promptBackup = prompt
    #promptBackup = binascii.hexlify(b(promptBackup))
    #if promptBackup in validPromptsHex:
    #    prompt = binascii.unhexlify(promptBackup)

    if prompt == 'C':
        prompt = input("\n    What would you like to copy? (RGB/HEX)\n    or type 'q' to cancel\n    ")
        prompt = str(prompt)
        prompt = prompt.upper()

        while prompt not in ['HEX', 'RGB', 'Q']:
            print('    Not a valid option!')
            prompt = input('    ')
            prompt = str(prompt)
            prompt = prompt.upper()

        if prompt == 'RGB':
            pyperclip.copy(rgbFinal)
            print('    RGB value has been copied to your clipboard!')

        elif prompt == 'HEX':
            pyperclip.copy(f'#{rgbHex}')
            print('    HEX value has been copied to your clipboard!')

        elif prompt == 'Q':
            prompt = 'ű'
            pass

    if prompt in saveAliases:
        hasSaved = True
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

        f = open(pathFullExt, 'w+')
        f.write(f'RGB: {rgbFinal}\n')
        f.write(f'HEX: #{rgbHex}')
        f.close()
        print(f'Color has been saved to {pathFullExt}')

    if prompt == 'Q':
        if hasSaved == False:
            promptSave = input('Are you sure you want to quit without saving? (y/n)\n')
            promptSave = promptSave.upper()

            while promptSave not in ['Y', 'N']:
                    promptSave = input('Not a valid option! (y/n)\n')
                    promptSave = promptSave.upper()

            if promptSave == 'Y':
                pass

            elif promptSave == 'N':
                prompt = 'ű'