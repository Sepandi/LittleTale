import pygame
from pygame import *
from Data.Engine.Window import *
class Render():
    onMenu = True
    Regular = font.Font("Data/Fonts/Regular.ttf",20)
    Bold = font.Font("Data/Fonts/Bold.ttf",20)
    Medium = font.Font("Data/Fonts/Medium.ttf",20)
    usernameFont = font.Font("Data/Fonts/PixelFont.ttf",7)
    LevelViewerFont = font.Font("Data/Fonts/PixelFont.ttf",18)
    DebugScreenFont = font.Font("Data/Fonts/PixelFont.ttf",15)
    hintsFont = font.Font("Data/Fonts/PixelFont.ttf",10)
    #--Text-Renderer
    font:font.Font
    def Text(fontName:font.Font,Word:str,Color,Position:Vector2,Window:pygame.Surface):
        #--Finds-Font-Type
        if fontName == Render.Regular:
            font = Render.Regular
        elif fontName == Render.Bold:
            font = Render.Bold
        elif fontName == Render.Medium:
            font = Render.Medium
        elif fontName == Render.usernameFont:
            font = Render.usernameFont
        elif fontName == Render.LevelViewerFont:
            font = Render.LevelViewerFont
        elif fontName == Render.DebugScreenFont:
            font = Render.DebugScreenFont
        elif fontName == Render.hintsFont:
            font = Render.hintsFont
        else:
            print("UNKNOWM FONT")
        #--Prints-The-Font
        Window.blit(font.render(Word,True,Color),Position)
    #--Draws-the-FPS-on-Window
    def PrintFPS(clock,win:pygame.Surface,Position:Vector2):
        Render.Text(Render.DebugScreenFont,"FPS:"+str(int(clock.getFPS())),(255,255,255),Position,win)
