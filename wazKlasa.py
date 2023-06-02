import pygame
import random
import wazz


class WazKlas():
    #konstruktor klasy - uruchamia się podczas tworzenia obiektu
    def __init__(self, rozdzielczosc):
        self.rozdzielczosc = rozdzielczosc
        self.pozycje=[(300,300)]
        self.dlugosc=1
        self.kierunek=[0,1]
        self.punkty=0
        self.kolor=(100, 100, 100)
    #ustalanie kierunku węża
    def setDirection(self, direction):
        self.kierunek=direction
    #pobieranie współrzednych głowy węża
    def getHeadPosition(self):
        return self.pozycje[-1]
    #wykonanie ruchu przez węża

    def ustawRozdzielczosc(self, rozdzielczosc):
        self.rozdzielczosc = rozdzielczosc

    def setColor(self, color):
        self.kolor = color

    def addScore(self):
        self.punkty +=1

    def clearScore(self):
        self.punkty = 0

    def addLength(self):
        self.dlugosc += 1

    def snakeMove(self):
        #pobranie ostatnie pozycji glowy węża
        ostatniaPozycja=self.getHeadPosition()
        self.checkCollision(ostatniaPozycja)
        #ustalenie nowej pozycji węża
        zmiennaX=ostatniaPozycja[0]+self.kierunek[0]*30
        zmiennaY=ostatniaPozycja[1]+self.kierunek[1]*30
        #sprawdzenie położenia weża względem krawędzi
        noweWspolrzedne=self.checkBorder(zmiennaX,zmiennaY)
        #dodanie pozycji węża do listy
        self.pozycje.append(noweWspolrzedne)
        #sprawdzenie czy wąż nie jest za długi
        if len(self.pozycje)>self.dlugosc:
            del self.pozycje[0]

    def checkCollision(self, pos):
        if pos in self.pozycje[:-1]:
            self.pozycje = [pos]
            self.dlugosc = 1
            self.punkty = 0            
    
    #sprawdzanie krawędzi okna
    def checkBorder(self,zmiennaX,zmiennaY):
         #sprawdzanie krawędzi
        if zmiennaX>=self.rozdzielczosc[0]:
            zmiennaX=0
        if zmiennaX<0:
            zmiennaX=600-30
        if zmiennaY>=self.rozdzielczosc[1]:
            zmiennaY=0
        if zmiennaY<0:
            zmiennaY=600-30
        return (zmiennaX,zmiennaY)
    #rysowanie węża
    def snakeDraw(self,oknoGry):
        for poz in self.pozycje[::-1]:
        #definiujemy kształ węża
            ksztaltWaz=pygame.Rect((poz[0],poz[1]),(30,30))
            #dodanie kształtu do okienka
            pygame.draw.rect(oknoGry,(self.kolor),ksztaltWaz)

    def getPunkty(self):
        return self.punkty

    def pozarcie(self, pozycjaGlowy):
        for czesciCiala in self.pozycje[::]:
            if pozycjaGlowy[0] == czesciCiala[0] and pozycjaGlowy[1] == czesciCiala[1]:
                self.dlugosc = 1
                self.punkty = 0
                self.pozycje = [(random.randint(0,wazz.rozdzialczosc)*30, random.randint(0,wazz.rozdzialczosc)*30)]
                