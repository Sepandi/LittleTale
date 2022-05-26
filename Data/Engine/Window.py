import pygame
from pygame import *
from Data.Engine.SpriteSheet import *
#--makes-pygame-easier( aka : just wanted to remove pygame from game.py XD)
class Window():
	#--Initializes-pygame
    def INIT():
        pygame.init()
    #--Makes-a-window-also-returns-window-for-(win.blit)
    def WinInit(WindowName:str,width:int,height:int):
        win = pygame.display.set_mode((width,height),HWSURFACE|DOUBLEBUF,64)
        display.set_caption(WindowName)
        display.set_icon(image.load("Data/Assets/UI/icon.png"))
        return win
    #--Closes-the-window-when-window-close-button-get-pressed(REQUAIERD)
    def CloseOnExit():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                for x in range(8):
                    print("\n")
                print("DONE")
                exit()
    #--Updates-The-Window(REQUAIERD)
    def Update():
        pygame.display.update()

#--Makes-a-pygame-clock
class Clock():
    def __init__(self):
        self.clock = pygame.time.Clock()
    #-returns-FPS
    def getFPS(self):
        return self.clock.get_fps()
