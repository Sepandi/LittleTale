import pygame
from pygame import *
class SpriteSheet():
    def __init__(self,FilePath):
        self.sheet = image.load(FilePath).convert_alpha()   
    def loadSprite(self,rectangle):
        rectangle = pygame.Rect(rectangle)
        image = pygame.Surface(rectangle.size).convert_alpha()   
        image.blit(self.sheet, (0, 0), rectangle)
        return image