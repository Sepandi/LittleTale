import pygame
from pygame import *
from Data.Engine.GameTime import GameTime
from Data.Engine.SpriteSheet import *
class Player():
    def __init__(self,x,y,username:str):
        self.health = 5
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = 2
        self.moving = False
        self.facingStatus = "down"
        self.facingRight = True
        self.score = 0
        #-Load-Sprites-of-Hearts-----------------------------
        self.heart = image.load("Data/Assets/UI/heart.png").convert_alpha()   
        #--Player-Sprites-(down,left,right)
        self.idle = image.load("Data/Assets/Player/player1.png").convert_alpha()   
        self.running1 = image.load("Data/Assets/Player/player2.png").convert_alpha()   
        self.running2 = image.load("Data/Assets/Player/player3.png").convert_alpha()    
        #--Player-Sprites-(up)
        self.idleUp = image.load("Data/Assets/Player/playerUp1.png").convert_alpha()   
        self.running1Up = image.load("Data/Assets/Player/playerUp2.png").convert_alpha()   
        self.running2Up = image.load("Data/Assets/Player/playerUp3.png").convert_alpha()   
        self.username = username
        #--Sword-Rect
        self.swordRect= Rect(1000,1000,32,32)
        self.onAtack = False
        #--Sword-Sprites
        self.swordRight = image.load("Data/Assets/Player/Sword1.png").convert_alpha()   
        self.swordLeft = transform.flip(self.swordRight,True,False)
        self.swordUp = image.load("Data/Assets/Player/Sword2.png").convert_alpha()   
        self.swordDown = transform.flip(self.swordUp,False,True)

    #--What-will-happen-when-player-gets-hurt-by-spicific-enemy-(must-used-in-enemy-classes)
    def Hurt(self):
        self.health -= 1
        mixer.music.load("Data/Sounds/damaged.wav")
        mixer.music.play()
    def Respawn(self,x,y):
        self.health = 5
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        
    def Update(self,win:Surface):
        #--KeyBinds
        KeyPress = pygame.key.get_pressed()
        if not self.onAtack:
            if KeyPress[K_w] or KeyPress[K_UP]:
                self.facingStatus = "up"
                self.moving = True
                self.rect.y -= self.speed
            elif KeyPress[K_s] or KeyPress[K_DOWN]:
                self.facingStatus = "down"
                self.moving = True
                self.rect.y += self.speed
            elif KeyPress[K_a] or KeyPress[K_LEFT]:
                self.facingStatus = "left"
                self.moving = True
                self.rect.x -= self.speed
                self.facingRight = False
            elif KeyPress[K_d] or KeyPress[K_RIGHT]:
                self.facingStatus = "right"
                self.moving = True
                self.rect.x += self.speed
                self.facingRight = True
            else :
                self.moving = False
        
        #--Sword-Updates
        if KeyPress[K_SPACE] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2] or pygame.mouse.get_pressed()[0]:
            self.moving = False
            self.onAtack = True
            if self.facingStatus == "up":
                self.swordRect.x = self.rect.x
                self.swordRect.y = self.rect.y - 32
                win.blit(self.swordUp,self.swordRect)
            if self.facingStatus == "down":
                self.swordRect.x = self.rect.x
                self.swordRect.y = self.rect.y + 32
                win.blit(self.swordDown,self.swordRect)
            if self.facingStatus == "right":
                self.swordRect.x = self.rect.x + 32
                self.swordRect.y = self.rect.y
                win.blit(self.swordRight,self.swordRect)
            if self.facingStatus == "left":
                self.swordRect.x = self.rect.x - 32
                self.swordRect.y = self.rect.y
                win.blit(self.swordLeft,self.swordRect)
        else:
            self.onAtack = False
            self.swordRect.x = 1000
            self.swordRect.y = 1000

        #--Set-Border
        if self.rect.x <= 28:
            self.rect.x = 28
        if self.rect.y <= 32:
            self.rect.y = 32
        if self.rect.x >= 580:
            self.rect.x = 580
        if self.rect.y >= 576:
            self.rect.y = 576

        self.Draw(win)
    
    def Draw(self,win:Surface):
        #usernamePanel = Render.usernameFont.render(self.username,True,(0,0,0))
        #win.blit(usernamePanel,(self.rect.x+(self.rect.width/2)-(usernamePanel.get_width()/2),self.rect.y-(usernamePanel.get_height()+5)))
        
        #--Drawing-Hearts
        for x in range(self.health):
            win.blit(self.heart,Vector2(28+(x*40),671))

        #--Player-Animation---------------------------
        if self.facingStatus == "up":
            if self.moving:
                if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                    win.blit(self.running1Up, self.rect)
                if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                    win.blit(self.idleUp, self.rect)
                if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                    win.blit(self.idleUp, self.rect)
                if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                    win.blit(self.running2Up, self.rect)
            else:
                win.blit(self.idleUp, self.rect)
        elif self.facingStatus == "down":
            if self.moving:
                if self.facingRight:
                    if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                        win.blit(self.idle, self.rect)
                    if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                        win.blit(self.running1, self.rect)
                    if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                        win.blit(self.idle, self.rect)
                    if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                        win.blit(self.running2, self.rect)
                elif not self.facingRight:
                    if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                        win.blit(transform.flip(self.idle ,True,False), self.rect)
                    if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                        win.blit(transform.flip(self.running1 ,True,False), self.rect)
                    if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                        win.blit(transform.flip(self.idle ,True,False), self.rect)
                    if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                        win.blit(transform.flip(self.running2 ,True,False), self.rect)
            else:
                if self.facingRight:
                    win.blit(self.idle, self.rect)
                elif not self.facingRight:
                    win.blit(transform.flip(self.idle ,True,False), self.rect)
        elif self.facingStatus == "left":
            if self.moving:
                if GameTime.timer >= 0 and GameTime.timer <= 0.08:
                    win.blit(transform.flip(self.running1 ,True,False), self.rect)
                if GameTime.timer >= 0.08 and GameTime.timer <= 0.16:
                    win.blit(transform.flip(self.idle ,True,False),self.rect)
                if GameTime.timer >= 0.16 and GameTime.timer <= 0.24:
                    win.blit(transform.flip(self.running2 ,True,False),self.rect)
            else:
                win.blit(transform.flip(self.idle,True,False),self.rect)
        elif self.facingStatus == "right":
            if self.moving:
                if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                    win.blit(self.idle,self.rect)
                if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                    win.blit(self.running1,self.rect)
                if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                    win.blit(self.idle,self.rect)
                if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                    win.blit(self.running2,self.rect)
            else:
                win.blit(self.idle,self.rect)
