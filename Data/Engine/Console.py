import pygame
from pygame import *
from Data.Engine.Levels import LevelManager
from Data.Engine.Window import *
class Console():
    onConsole = False
    def CheckForConsoleRequests():
        KeyPress =  key.get_pressed()
        if KeyPress[K_t]:
            Console.onConsole = True
            while Console.onConsole:
                Window.CloseOnExit()
                Input = input("Enter a command: ")
                if Input == "quit":
                    pygame.quit()
                    quit()
                elif Input == "levelup":
                    LevelManager.NextLevel()
                    print("set level to: "+str(LevelManager.GetLevel()))
                elif Input == "setLevel":
                    setLevel = input("Enter The Level")
                    number = int(setLevel)
                    if number >= -5 and number <= 0:
                        LevelManager.level = number
                    

                else:
                    print("Invalid command")
                    Console.onConosole = False
                Console.onConsole = False
