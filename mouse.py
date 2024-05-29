from pynput.mouse import Controller
from time import sleep
from sys import argv
import random, signal, sys, ctypes

def handler(sig, frame):
    print("Cerrando aplicacion")
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

def moveMouse(mouse, seconds):
    while True:
        print("\nMoviendo")
        ancho, alto = getDimensions();
        mouse.position = (ancho,alto)
        sleep(2)
        moveX = random.randint(80,ancho-80)    
        moveY = random.randint(80,alto-80)
        mouse.move(moveX,moveY)
        print(moveX,moveY)
        sleep(seconds - 2)

def getSeconds():
    seconds = 165
    if len(argv) == 2:
        seconds = argv[1]
    return int(seconds) * 60;

def getDimensions():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = int(user32.GetSystemMetrics(0)/2), int(user32.GetSystemMetrics(1)/2)
    return [ancho, alto]

if __name__ == "__main__":
    mouse = Controller()
    moveMouse(mouse, getSeconds())