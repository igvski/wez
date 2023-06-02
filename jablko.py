import random
import pygame
import wazz

class Jablko():
    def __init__(self, rozdzielczosc):
        self.rozdzielczosc = (rozdzielczosc[0]/30, rozdzielczosc[1]/30)
        self.pozycja = [(1,1)]
        self.randomPosition()
        self.getPosition()

    def ustawRozdzielczosc(self, rozdzielczosc):
        self.rozdzielczosc = rozdzielczosc


    def randomPosition(self):
        jablkoX=random.randint(0,self.rozdzielczosc[0])*30
        jablkoY=random.randint(0,self.rozdzielczosc[1])*30
        self.setPosition(jablkoX, jablkoY)

    def getPosition(self):
        return self.pozycja[-1]

    def setPosition(self, x, y):
        self.pozycja[0] = (x, y)

    def drawApple(self, oknoGry):
        pygame.draw.circle(oknoGry,(255,0,0),(self.pozycja[0][0]+15,self.pozycja[0][1]+15),15)