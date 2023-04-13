import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    #for cactus 
    for i in range(300,415):
        for j in range(563,650):
            if data[i,j] < 100:
                hit("up")
                return
    #for birds        
    for i in range(300,415):
        for j in range(410,563):
            if data[i,j] < 100:
                hit("down")
                return 
    return            
if __name__=="__main__":
    print("Hey!!..The game is about to start in 3 seconds")
    time.sleep(3)
    #hit("space")


    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
        #draw rectangle for cactus
        '''
        for i in range(300,415):
            for j in range(563,650):
                data[i,j]=0

        #rectangle for bird
        for i in range(300,415):
            for j in range(410,563):
                data[i,j]=172
        image.show()        
        '''