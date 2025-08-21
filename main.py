import keyboard
from mouseMove import coloredAll
from settings import DELAY, STEP_CHANGE_DELAY

isAppRun = True
isScriptRun = False

def mainLoop():
    global isAppRun, isScriptRun

    print("Halloo!")
    print("Press C for Start or Pause Script")
    print("Press X for end App")
    print("Press T for up speed")
    print("Press G for down speed\n")

    while isAppRun:
        while isScriptRun:
            coloredAll()
            isScriptRun = False

def endApp():
    print("Sayonara")
    global isAppRun
    isAppRun = False

def pauseApp():
    global isScriptRun
    print("Pause..") if isScriptRun else print("Continue..")
    isScriptRun = not isScriptRun 

def upSpeed():
    global DELAY
    DELAY = max(0, DELAY - STEP_CHANGE_DELAY)
    print("Delay: ", round(DELAY, 5))

def downSpeed():
    global DELAY
    DELAY += STEP_CHANGE_DELAY
    print("Delay: ", round(DELAY, 5))

def setup():
    keyboard.add_hotkey('X', endApp)
    keyboard.add_hotkey('C', pauseApp)
    keyboard.add_hotkey('T', upSpeed)
    keyboard.add_hotkey('G', downSpeed)

if (__name__ == "__main__"):
    setup()
    mainLoop()