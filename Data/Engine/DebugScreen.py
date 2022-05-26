from platform import platform
import pygame
from pygame import *
from Data.Engine.Player import *
from Data.Engine.Render import *
from Data.Engine.Levels import *
import platform

background = image.load("Data/Assets/UI/debugMenu.png")
class DebugScreen():
    def update(win,clock,player,GAME_VERSION):
        KeyPress = pygame.key.get_pressed()
        if KeyPress[K_F3]:
            win.blit(background,(0,0))
            Render.Text(Render.DebugScreenFont,f"Little Tale - {GAME_VERSION}",(255,255,255),Vector2(20,10),win)
            Render.PrintFPS(clock,win,Vector2(20,25))
            Render.Text(Render.DebugScreenFont,f"OS:{platform.system()}/{platform.machine()}",(255,255,255),Vector2(20,40),win)
            Render.Text(Render.DebugScreenFont,f"Client:{platform.python_implementation().capitalize()}/{platform.python_version()}",(255,255,255),Vector2(20,55),win)
            Render.Text(Render.DebugScreenFont,f"XY:{player.rect.x},{player.rect.y}",(255,255,255),Vector2(20,85),win)
            