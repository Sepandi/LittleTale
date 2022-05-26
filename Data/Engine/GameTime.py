from telnetlib import GA


class GameTime():
    #--Sets-The-Timer-And-Recevies-the-Delta-Time-From-game.py
    timer = 0.24
    deltaTime = 0
    playerCanDamage = 2
    def Update():
        #--sets-and-resets-the-timer
        GameTime.timer -= GameTime.deltaTime
        if GameTime.timer <= 0:
            GameTime.timer = 0.24

        #--sets-and-resets-the-player-damage-timer
        GameTime.playerCanDamage -= GameTime.deltaTime
        if GameTime.playerCanDamage <= 0:
            GameTime.playerCanDamage = 2
        
