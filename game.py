#  pygame 2.1.2
#--Initializes-Window
from Data.Engine.Window import *
from pygame import *
Window.INIT()
#--Setup-Window-------------------------------------------
GAME_VERSION = "1.0"
win = Window.WinInit(f"Little Tale : Tiny Escaper - {GAME_VERSION}",640,730)
mixer.init()
#--Import-Engine-Modules--------------------------
from Data.Engine.Player import Player
from Data.Engine.Render import Render  
from Data.Engine.Ladders import *
from Data.Engine.Console import Console
from Data.Engine.GameTime import GameTime
from Data.Engine.Levels import *
from Data.Engine.DebugScreen import *
from Data.Engine.SpriteSheet import *
#--On-Load------------------------------------------------------------
#--Setup-Menu
from pygame import image
from pygame.key import *
onMenu = "onMenu"
menu = image.load("Data/Assets/UI/Menu.png")
#--Clock
clock = Clock()
#--Make-Player
player = Player(500,500,"Sepandi")
#--Make-Ladders
ladderUp = LadderUp(32,32)
ladderDown = LadderDown(576,580)
#--Load-UI
background = image.load("Data/Assets/UI/bg.png").convert_alpha()
panel = image.load("Data/Assets/UI/panel.png").convert_alpha()
#--Main-Loop----------------------------------------------------------
#--Update-------------------------------------------------------------
while 1:
    if onMenu == "onMenu":
        if key.get_pressed()[K_RETURN]:
            onMenu = "onGame"
        win.blit(menu,(0,0))
        Render.Text(Render.DebugScreenFont,"\xa9 2022 Sepandi",(230,160,102),Vector2(320,320),win)
        Render.Text(Render.LevelViewerFont,"Press Enter to Start",(230,160,102),Vector2(140,500),win)
    elif onMenu == "onGame":
        if key.get_pressed()[K_ESCAPE]:
            onMenu = "onMenu"
        #--Render-UI
        if LevelManager.level == -5:
            Render.Text(Render.hintsFont,"Press SPACE or Mouse Buttons to use the Sword",(89,86,82),Vector2(100,500),win)
        win.blit(background,(0,0))
        win.blit(panel,(0,640))
        Render.Text(Render.LevelViewerFont,"Level:"+str(LevelManager.GetLevel()),(217,160,102),Vector2(250,675),win)
        Render.Text(Render.LevelViewerFont,"Score:"+str(player.score),(230,160,102),Vector2(450,675),win)
        #--Update-Entities
        ladderUp.Update(win,player.rect,ladderDown.rect)
        ladderDown.Update(win,player.rect,ladderUp.rect)
        player.Update(win)
        #--Respawn-Player
        if player.health <= 0:
            levelsToBack = 5 + LevelManager.GetLevel()
            for i in range(levelsToBack):
                LevelManager.PreviousLevel()
            player.Respawn(500,500)
        #--Update-Levels
        LevelManager.update(win,player)
        #--Check-for-console
        Console.CheckForConsoleRequests()
        #--Update-Debug-Screen
        DebugScreen.update(win,clock,player,GAME_VERSION)
    #--Important-Stuff
    Window.CloseOnExit()
    Window.Update()
    win.fill((255,255,255))
    GameTime.deltaTime = clock.clock.tick(60) / 1000  
    GameTime.Update()