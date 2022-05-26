from re import U
import pygame 
from pygame import *
from Data.Engine.Levels import LevelManager
from Data.Engine.SpriteSheet import SpriteSheet
from Data.Engine.Render import Render
#--The-Ladder-that-takes-the-player-one-level-up
class LadderUp():
    def __init__(self,x,y):
        self.image = image.load("Data/Assets/Ladders/ladderUp.png").convert_alpha()
        self.rect = Rect(x,y,self.image.get_width(),self.image.get_height())
        
    def Update(self,window:Surface,playerRect:Rect,DownerLadder:Rect):
        #--Checks-the-colid-with-player-and-also-checks-the-key-button
        if LevelManager.level <= -1:
            KeyPress = pygame.key.get_pressed()
            if self.rect.colliderect(playerRect):
                hint = Render.usernameFont.render("Press Space to Use",True,(255,255,255))
                draw.rect(window,(155,173,183),Rect(self.rect.x+33,self.rect.y+8,hint.get_width()+2,hint.get_height()+6))
                window.blit(hint,(self.rect.x+35,self.rect.y+10))
                if KeyPress[K_SPACE] :
                    LevelManager.NextLevel()
                    playerRect.x = DownerLadder.x
                    playerRect.y = DownerLadder.y - 40
            self.Draw(window)
    def Draw(self,window:Surface):
        window.blit(self.image,self.rect)


#--The-Ladder-that-takes-the-player-down
class LadderDown():
    def __init__(self,x,y):
        self.image = image.load("Data/Assets/Ladders/ladderDown.png").convert_alpha()
        self.rect = Rect(x,y,self.image.get_width(),self.image.get_height())
    #--Checks-the-colid-with-player-and-also-checks-the-key-button
    def Update(self,window:Surface,playerRect:Rect,UpperLadder:Rect):
        if LevelManager.level >= -4:
            KeyPress = pygame.key.get_pressed()
            if self.rect.colliderect(playerRect):
                hint = Render.usernameFont.render("Press Space to Use",True,(255,255,255))
                draw.rect(window,(155,173,183),Rect(self.rect.x-122,self.rect.y-10,hint.get_width()+2,hint.get_height()+8))
                window.blit(hint,(self.rect.x-120,self.rect.y-8))
                if KeyPress[K_SPACE]:
                    LevelManager.PreviousLevel()
                    playerRect.x = UpperLadder.x
                    playerRect.y = UpperLadder.y + 40
            self.Draw(window)
    def Draw(self,window:Surface):
        window.blit(self.image,self.rect)   
            

            

