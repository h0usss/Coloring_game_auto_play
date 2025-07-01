import keyboard
import mouse
import pyautogui 
import time
from PIL import Image, ImageGrab
from settings import *

isRun = True
delay = 0.1

def coloredAll():
    setup()

    field = getWindowImage()
    
    while isHaveNonColored(field, ImageGrab.grab().crop(field)):
        image = ImageGrab.grab().crop(field)

        for x in range(field[0], field[2], CELL_SIZE):
            for y in range(field[1], field[3], CELL_SIZE):
                pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

                if (pixel == COLOR_GREEN_CELL):
                    mouse.move(x + 1, y + 1)
                    mouse.click()
                    time.sleep(delay)
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
                time.sleep(delay)
                mouse.right_click()
                time.sleep(delay + 0.1)
                return True
            
            if (not isRun):
                return
            
    return False
        
def getWindowImage():
    window = pyautogui.getWindowsWithTitle("Coloring Game - Little City")[0]
    if window:
        left, top, width, height = window.left, window.top, window.width, window.height
        return [left, top, width - left, height - top]
    return None


def stopLoop():
    global isRun
    isRun = False

def setup():
    keyboard.add_hotkey('X', stopLoop)
    keyboard.add_hotkey('C', stopLoop)
