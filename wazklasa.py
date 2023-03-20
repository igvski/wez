class WazKlas():
    #konstruktor klasy - uruchamia się podczas tworzenia obiektu
    def __init__(self):
        self.pozycje[(300,300)]
        self.dlugosc=1
        self.kierunek=[0,1]
        self.punkty=0
    #ustalanie kierunku węża
    def setDirection(self, direction):
        self.kierunek=direction
    #pobrieranie współrzędnych głowy węża
    def getHeadPosition(self):
        return self.pozycje[-1]
    #wykonanie ruchu przez węża
    def snakeMove(self):
        #pobranie ostatnie pozycji głowy węża
        ostatniaPozycja=self.getHeadPosition()
        #ustalanie nowej pozycji węża
        zmiennaX=ostatniaPozycja[0]+self.kierunek[0]*30;
        zmiennaY=ostatniaPozycja[1]+self.kierunek[1]*30;