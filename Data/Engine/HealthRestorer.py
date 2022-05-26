from pygame import *
from Data.Engine.GameTime import GameTime
from Data.Engine.Ladders import *
from Data.Engine.Render import Render
#--Makes-a-zombie
class HealthRestorer():
    def __init__(self,x:int,y:int):
        self.health = 5
        self.rect = Rect(x,y,32,32)
        #---Sprites
        self.heart1 = image.load("Data/Assets/healthRestorer1.png").convert_alpha()
        self.heart2 = image.load("Data/Assets/healthRestorer2.png").convert_alpha()
    #--Updates-The-Zombie
    def Update(self,win:Surface,player):
        #--Set-Border
                
        #--Detects-Player
        if self.rect.colliderect(player):
            player.health = 5
            self.rect.x += 10000
            self.rect.y += 10000
        
        self.Draw(win) 
    def Draw(self,win):

            if GameTime.timer >= 0 and GameTime.timer <= 0.12:
                win.blit(self.heart1, self.rect)
            if GameTime.timer >= 0.12 and GameTime.timer <= 0.24:
                win.blit(self.heart2, self.rect)

        
