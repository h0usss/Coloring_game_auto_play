import keyboard
from mouseMove import coloredAll

isAppRun = True
isScriptRun = False

def mainLoop():
    global isAppRun, isScriptRun
    print("Halloo, press C for Start or Pause Script")
    print("Press X for end App")
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

def setup():
    keyboard.add_hotkey('X', endApp)
    keyboard.add_hotkey('C', pauseApp)

if (__name__ == "__main__"):
    setup()
    mainLoop()