from pygame import *
from Data.Engine.GameTime import GameTime
from Data.Engine.Ladders import *
from Data.Engine.SpriteSheet import SpriteSheet
from Data.Engine.Render import Render
damagingPlayerTimer = 1
#--Makes-a-zombie
class Zombie():
    def __init__(self,x:int,y:int):
        self.health = 5
        self.rect = Rect(x,y,32,32)
        self.speed = 1
        self.facingStatus = "right"
        self.playerDetector = Rect(self.rect.x-72,self.rect.y-72,(72*2)+32,(72*2)+32)
        self.playerDetectorImage = image.load("Data/Assets/UI/enemyPlayerDetector.png").convert_alpha()
        self.shouldFollowPlayer = False
        self.canTakeDamage = True
        #--Zombie-Sprites
        self.idle = image.load("Data/Assets/Enemies/Zombies/Zombie1.png").convert_alpha()
        self.running1 = image.load("Data/Assets/Enemies/Zombies/Zombie2.png").convert_alpha()
        self.running2 = image.load("Data/Assets/Enemies/Zombies/Zombie3.png").convert_alpha()
        #--Zombie-Sprites-UP
        self.idleUp = image.load("Data/Assets/Enemies/Zombies/ZombieUp1.png").convert_alpha()
        self.running1Up = image.load("Data/Assets/Enemies/Zombies/ZombieUp2.png").convert_alpha()
        self.running2Up = image.load("Data/Assets/Enemies/Zombies/ZombieUp3.png").convert_alpha()
        self.movingTimer = 10
    #--Updates-The-Zombie
    def Update(self,win:Surface,player):
    	#--Zombie's-AI :D
        self.movingTimer -= GameTime.deltaTime
        if not self.shouldFollowPlayer :
            if self.movingTimer <= 0 :
                self.movingTimer = 10
            if self.movingTimer <= 10 and self.movingTimer >= 7.5:
                self.rect.x += self.speed
                self.facingStatus = "right"
            if self.movingTimer <= 7.5 and self.movingTimer >= 5:
                self.rect.y += self.speed
                self.facingStatus = "down"
                
            if self.movingTimer <= 5 and self.movingTimer >= 2.5:
                self.rect.x -= self.speed
                self.facingStatus = "left"
            if self.movingTimer <= 2.5 and self.movingTimer >= 0:
                self.rect.y -= self.speed
                self.facingStatus = "up"
        elif self.shouldFollowPlayer:
            if self.rect.x < player.rect.x :
                self.rect.x += self.speed
                self.facingStatus = "right"
            elif self.rect.x > player.rect.x :
                self.rect.x -= self.speed
                self.facingStatus = "left"
            if self.rect.y < player.rect.y and self.rect.x == player.rect.x :
                self.rect.y += self.speed
                self.facingStatus = "down"
            elif self.rect.y > player.rect.y and self.rect.x == player.rect.x :
                self.rect.y -= self.speed
                self.facingStatus = "up"
        #--Set-Border
        if self.health > 0:
            if self.rect.x <= 28:
                self.rect.x = 28
            if self.rect.y <= 32:
                self.rect.y = 32
            if self.rect.x >= 580:
                self.rect.x = 580
            if self.rect.y >= 576:
                self.rect.y = 576
                
        #--Detects-Player-if-the-player-is-around
        if self.playerDetector.colliderect(player):
            self.shouldFollowPlayer = True
        else :
            self.shouldFollowPlayer = False


        #--Deal-Damage-To-Player
        if self.rect.colliderect(player.rect):
            if GameTime.playerCanDamage <= 2 and GameTime.playerCanDamage >= 1.9999999999999999:
                player.Hurt()
        #--Take-Damege
        if self.rect.colliderect(player.swordRect):
            if self.canTakeDamage:
                self.canTakeDamage = False
                self.health -= 1
                mixer.music.load("Data/Sounds/Attack.wav")
                mixer.music.play()
            if self.health <= 0 :
                self.health = 0
                self.rect.x = -1000
                self.rect.y = 0
                player.score += 10
                mixer.music.load("Data/Sounds/Score.wav")
                mixer.music.play()
        else :
            self.canTakeDamage = True



        #--Set-Player-Detector
        self.playerDetector.x = self.rect.x-64
        self.playerDetector.y = self.rect.y-64
        self.Draw(win)
	#--Draws-The-Zombie-Like-Players-Animation
    def Draw(self,win):
        KeyPress = pygame.key.get_pressed()
        if KeyPress[K_F3]:
            win.blit(self.playerDetectorImage,self.playerDetector)
            healthPanel = Render.usernameFont.render(str(self.health),True,(0,0,0))
            win.blit(healthPanel,(self.rect.x+(self.rect.width/2)-(healthPanel.get_width()/2),self.rect.y-(healthPanel.get_height()+5)))
        #--Zombies-Animation
        if self.facingStatus == "up":
            if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                win.blit(self.running1Up, self.rect)
            if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                win.blit(self.idleUp, self.rect)
            if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                win.blit(self.idleUp, self.rect)
            if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                win.blit(self.running2Up, self.rect)
        elif self.facingStatus == "down":
                if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                    win.blit(self.idle, self.rect)
                if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                    win.blit(self.running1, self.rect)
                if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                    win.blit(self.idle, self.rect)
                if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                    win.blit(self.running2, self.rect)
        elif self.facingStatus == "left":
            if GameTime.timer >= 0 and GameTime.timer <= 0.08:
                win.blit(transform.flip(self.running1 ,True,False), self.rect)
            if GameTime.timer >= 0.08 and GameTime.timer <= 0.16:
                win.blit(transform.flip(self.idle ,True,False),self.rect)
            if GameTime.timer >= 0.16 and GameTime.timer <= 0.24:
                win.blit(transform.flip(self.running2 ,True,False),self.rect)
        elif self.facingStatus == "right":
            if GameTime.timer >= 0 and GameTime.timer <= 0.06:
                win.blit(self.idle,self.rect)
            if GameTime.timer >= 0.06 and GameTime.timer <= 0.12:
                win.blit(self.running1,self.rect)
            if GameTime.timer >= 0.12 and GameTime.timer <= 0.18:
                win.blit(self.idle,self.rect)
            if GameTime.timer >= 0.18 and GameTime.timer <= 0.24:
                win.blit(self.running2,self.rect)

        
