import random
import pygame
#import kodu z klasą wąż
import wazKlasa
from jablko import Jablko

#tworzenie obiektu wąż
rozdzialczosc = 19
rozmiarOkna = (600,600)
obiektWaz1=wazKlasa.WazKlas(rozmiarOkna)
obiektWaz2=wazKlasa.WazKlas(rozmiarOkna)
iloscJablek = 1
def ustawKolorWaz1(kolor):
    obiektWaz1.setColor(kolor)

def ustawKolorWaz2(kolor):
    obiektWaz2.setColor(kolor)

def ustawRozmiar(rozmiar):
    rozmiarOkna = rozmiar
    print(rozmiarOkna[0], rozmiarOkna[1])

#utworzenie funkcji waz
def waz(rozmiar):
    obiektWaz1.ustawRozdzielczosc(rozmiarOkna)
    obiektWaz2.ustawRozdzielczosc(rozmiarOkna)    
    #inicjalizacja biblioteki
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode(rozmiarOkna,0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną, która przechowuje informacje czy gra jest uruchomiona
    run=True
   
    #pozycja startowa jabłka
    wszystkieJablka = []

    for numer in range(0, iloscJablek):
        wszystkieJablka.append(Jablko(rozmiarOkna))
    # jablko.randomPosition()
    # jablkoX=random.randint(0,19)*30
    # jablkoY=random.randint(0,19)*30
    # punkty=0

    #pętla while sprawdza czy warunek w zmiennej run jest prawdziwy, jak jest nieprawdziwy kończy swoje działanie
    while(run):
        #Wypełnienie okna kolorem
        oknoGry.fill((0,0,0))
        #ustawienie opóźnienia odświeżania gry
        pygame.time.delay(200)
        #sprawdzanie czy istnieją jakieś zdarzenia i zapisanie ich do zmiennej "zdarzenia"
        for zdarzenia in pygame.event.get():
            #jeżeli zmienna "zdarzenia" przechowuje naciśniecie przycisku zamknij to zmieniamy wartosć zmiennej "run"
            if zdarzenia.type==pygame.QUIT:
                run=False
                #obsługa zdarzeń klawiatury i zmiana pozycji węża
            elif zdarzenia.type==pygame.KEYDOWN:
                if zdarzenia.key==pygame.K_RIGHT:
                    obiektWaz1.setDirection([1,0])
                elif zdarzenia.key==pygame.K_LEFT:
                    obiektWaz1.setDirection([-1,0])
                elif zdarzenia.key==pygame.K_UP:
                    obiektWaz1.setDirection([0,-1])
                elif zdarzenia.key==pygame.K_DOWN:
                    obiektWaz1.setDirection([0,1])
                if zdarzenia.key==pygame.K_d:
                    obiektWaz2.setDirection([1,0])
                elif zdarzenia.key==pygame.K_a:
                    obiektWaz2.setDirection([-1,0])
                elif zdarzenia.key==pygame.K_w:
                    obiektWaz2.setDirection([0,-1])
                elif zdarzenia.key==pygame.K_s:
                    obiektWaz2.setDirection([0,1])
        #ustalenie nowej pozycji węża
        obiektWaz1.snakeMove()
        obiektWaz2.snakeMove()
                
        #pozycja głowy weza
        glowa=obiektWaz1.getHeadPosition()
        glowa2=obiektWaz2.getHeadPosition()
        #zjadanie jabłka
        for nrJablko in wszystkieJablka:
            pozycjaJablka = nrJablko.getPosition()
            if glowa[0]==pozycjaJablka[0] and glowa[1] == pozycjaJablka[1]:
                # jablkoX=random.randint(0,19)*30
                # jablkoY=random.randint(0,19)*30
                nrJablko.randomPosition()
                obiektWaz1.addScore()
                obiektWaz1.addLength()
                print(obiektWaz1.punkty, 1)
                print(obiektWaz2.punkty, 2)

            if glowa2[0]==pozycjaJablka[0] and glowa2[1] == pozycjaJablka[1]:
                # jablkoX=random.randint(0,19)*30
                # jablkoY=random.randint(0,19)*30
                nrJablko.randomPosition()
                obiektWaz2.addScore()
                obiektWaz2.addLength()
                print(obiektWaz1.punkty, 1)
                print(obiektWaz2.punkty, 2)

            nrJablko.drawApple(oknoGry)
        #rysowanie jabłka
        # pygame.draw.circle(oknoGry,(255,0,0),(jablkoX+15,jablkoY+15),15)
        #rysowanie węża

        obiektWaz1.pozarcie(glowa2)
        obiektWaz2.pozarcie(glowa)

        obiektWaz1.snakeDraw(oknoGry)
        obiektWaz2.snakeDraw(oknoGry)


       
        #napisy na ekranie
        czcionka=pygame.font.SysFont('arial',25)
        tekst=czcionka.render("Zdobyłeś punkty: {0}".format(obiektWaz1.punkty),1,(51,51,255))
        tekst2=czcionka.render("Zdobyłeś punkty: {0}".format(obiektWaz2.punkty),1,(51,51,255))
        oknoGry.blit(tekst,(10,10))
        oknoGry.blit(tekst2,(300,10))
        #aktualizowanie zawartości okna gry
        pygame.display.update()


#wywołanie funkcji, pozwala na uruchomienie gry
# waz()