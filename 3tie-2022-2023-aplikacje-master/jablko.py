import random


class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.pozycjaJablka=[(1,1)]
        self.randomPosition()
    #losowanie pozycji jabłka i zapisanie nowej pozycji do zmiennej pozycjaJablka
    def randomPosition(self):
        jablkoX=random.randint(0,19)*30
        jablkoY=random.randint(0,19)*30

    #pobieranie pozycji jabłka
    def getCoordinates(self):
        return self.pozycjaJablka[-1]
    
    #ustawieanie pozycji jabłka
    def setCoordinates(self,x,y):
        self.pozycjaJablka[0]=(x,y)