import keyboard
import mouse
import pyautogui 
import time
from PIL import ImageGrab
from settings import *

isRun = True

def coloredAll():
    setup()

    field = getWindowImage()

    if (not field):
        print("The game window was not found")
        return
    
    while isHaveNonColored(field, ImageGrab.grab().crop(field)):
        image = ImageGrab.grab().crop(field)

        for x in range(field[0], field[2], CELL_SIZE):
            for y in range(field[1], field[3], CELL_SIZE):
                pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

                if (pixel in COLOR_SELECTED_CELL):
                    mouse.move(x + 1, y + 1)
                    mouse.click()
                    time.sleep(DELAY)
                    image = ImageGrab.grab().crop(field)
                
                if (not isRun):
                    return
                
                
def getPixelCollorToHex(x, y, image):
    r, g, b = image.getpixel((x, y))

    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def isHaveNonColored(field, image):
    global isRun
    isRun = True
    for x in range(field[0], field[2], CELL_SIZE):
        for y in range(field[1], field[3], CELL_SIZE):
            pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

            if (pixel == COLOR_CELL):
                mouse.move(x + 2, y + 2)
                time.sleep(DELAY)
                mouse.right_click()
                time.sleep(DELAY + 0.1)
                return True
            
            if (not isRun):
                return
            
    return False
        
def getWindowImage():
    for win in WIN_NAME:

        window = pyautogui.getWindowsWithTitle(win)

        if window:
            left, top, width, height = window[0].left, window[0].top, window[0].width, window[0].height
            return [left, top, width - left, height - top]
        
    return None


def stopLoop():
    global isRun
    isRun = False

def upSpeed():
    global DELAY
    DELAY = max(0, DELAY - STEP_CHANGE_DELAY)
    print("Delay: ", round(DELAY, 5))

def downSpeed():
    global DELAY
    DELAY += STEP_CHANGE_DELAY
    print("Delay: ", round(DELAY, 5))

def setup():
    keyboard.add_hotkey('X', stopLoop)
    keyboard.add_hotkey('C', stopLoop)
    keyboard.add_hotkey('T', upSpeed)
    keyboard.add_hotkey('G', downSpeed)
