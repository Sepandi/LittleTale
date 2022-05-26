from pygame import *
from Data.Engine.Zombie import Zombie
from Data.Engine.HealthRestorer import HealthRestorer
import random
from Data.Engine.Render import Render
class LevelManager():
    #--Default-Level-to-Start
    level = -5
    def NextLevel():
        LevelManager.level += 1
    def PreviousLevel():
        LevelManager.level -= 1
    def GetLevel():
        return LevelManager.level
    def update(win:Surface,player:Rect):
        #--Used-to-Update-The-Levels
        #--A-very-easy-methode
        if LevelManager.level == -5:
            LevelMinusFive.zombie1.Update(win,player)
        if LevelManager.level == -4:
            LevelMinusFour.zombie1.Update(win,player)
            LevelMinusFour.zombie2.Update(win,player)
            LevelMinusFour.zombie3.Update(win,player)
        if LevelManager.level == -3:
            LevelMinusThree.zombie1.Update(win,player)
            LevelMinusThree.zombie2.Update(win,player)
            LevelMinusThree.zombie3.Update(win,player)
            LevelMinusThree.restorer.Update(win,player)
        if LevelManager.level == -2:
            LevelMinusTwo.zombie1.Update(win,player)
            LevelMinusTwo.zombie2.Update(win,player)
            LevelMinusTwo.zombie3.Update(win,player)
        if LevelManager.level == -1:
            LevelMinusOne.zombie1.Update(win,player)
            LevelMinusOne.zombie2.Update(win,player)
            LevelMinusOne.zombie3.Update(win,player)
            LevelMinusOne.restorer.Update(win,player)
        if LevelManager.level == 0:
            Render.Text(Render.hintsFont,"You Did it ! Game is Finished !",(89,86,82),Vector2(100,100),win)
            Render.Text(Render.hintsFont,"Remember Its just a Prototype!",(89,86,82),Vector2(100,150),win)
            Render.Text(Render.hintsFont,"Full Game will Come Soon! at github.com/Sepandi",(89,86,82),Vector2(100,200),win)
#--Initalize-Entities-For-Each-level
class LevelMinusFive():
    zombie1 = Zombie(100,100)
class LevelMinusFour():
    zombie1 = Zombie(700,300)
    zombie2 = Zombie(400,400)
    zombie3 = Zombie(200,500)
class LevelMinusThree():
    restorer = HealthRestorer(random.randint(32,300),random.randint(32,300))
    zombie1 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie2 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie3 = Zombie(random.randint(0,700),random.randint(0,700))
class LevelMinusTwo():
    zombie1 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie2 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie3 = Zombie(random.randint(0,700),random.randint(0,700))
class LevelMinusOne():
    restorer = HealthRestorer(random.randint(32,300),random.randint(32,300))
    zombie1 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie2 = Zombie(random.randint(0,700),random.randint(0,700))
    zombie3 = Zombie(random.randint(0,700),random.randint(0,700))
