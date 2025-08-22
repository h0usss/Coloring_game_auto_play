import time
import mouse
import keyboard
import pyautogui 
from settings import *
from PIL import ImageGrab, ImageChops, Image

isStopLoop = False

def coloredAll():    
    direction = 'r'

    setup()
    field = getWindowImage()
    
    if (field is None):
        print("The game window was not found")
        return -1 
    
    while True:
        if (isHaveNonColored(field, ImageGrab.grab().crop(field))):
            changeFillColor(field, ImageGrab.grab().crop(field))
            image = ImageGrab.grab().crop(field)

            for x in range(field[0], field[2], CELL_SIZE):
                for y in range(field[1], field[3], CELL_SIZE): 

                    if isStopLoop: return

                    pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

                    if (pixel in COLOR_SELECTED_CELL):
                        mouse.move(x + 1, y + 1)
                        mouse.click()
                        time.sleep(DELAY)                                          
                        image = ImageGrab.grab().crop(field)                    
        else:
            if isStopLoop: return

            move(direction)
            if not (isHaveNonColored(field, ImageGrab.grab().crop(field))):
                move('d')
                direction = 'l' if direction == 'r' else 'r'
                
                
def getPixelCollorToHex(x, y, image):
    r, g, b = image.getpixel((x, y))
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def isHaveNonColored(field, image):
    for x in range(field[0], field[2], CELL_SIZE):
        for y in range(field[1], field[3], CELL_SIZE):
            pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

            if pixel == COLOR_CELL: 
                return True
                        
    return False

def changeFillColor(field, image):
    for x in range(field[0], field[2], CELL_SIZE):
        for y in range(field[1], field[3], CELL_SIZE):
            pixel = getPixelCollorToHex(x - field[0] , y - field[1], image)

            if pixel == COLOR_CELL:
                mouse.move(x + 2, y + 2)
                time.sleep(DELAY)
                mouse.right_click()
                time.sleep(DELAY + 0.1)
                mouse.click()
                return True
            
    return False
        
def getWindowImage():
    for win in WIN_NAME:

        window = pyautogui.getWindowsWithTitle(win)

        if window:
            field = [window[0].left, window[0].top, window[0].width, window[0].height]
            coordsHelper = find_image(ImageGrab.grab().crop(field), Image.open("img/button.png"))
            
            if (coordsHelper):
                field[2] = coordsHelper[0]
                field[3] = coordsHelper[1]

            return field
        
    return None

def find_image(big, small):
    print("Try to find canvas..")
    bw, bh = big.size
    sw, sh = small.size

    big = big.convert("RGB")
    small = small.convert("RGB")

    for x in range(bw - sw + 1, 0, -1):
        for y in range(bh - sh + 1):
            if isStopLoop: return

            box = (x, y, x + sw, y + sh)
            region = big.crop(box)

            diff = ImageChops.difference(region, small)
            if not diff.getbbox():
                return [x + sw, y + sh]
            
    return None

def move(direction_):
    direction = ""

    match(direction_):
        case 'u': direction = "up"
        case 'r': direction = "right"
        case 'b' | 'd': direction = "down"
        case 'l': direction = "left"
        case _ : raise IOError("Unknown direction")
        
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown(direction)
    time.sleep(1)    
    pyautogui.keyUp(direction)
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("ctrl")

def stopLoop():
    global isStopLoop
    isStopLoop = True

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