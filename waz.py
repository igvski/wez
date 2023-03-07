#pobranie biblioteki pygame
import random
import pygame

#utworzenie funkcji waz
def waz():
    #inicjalizacja biblioteki
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną, która przechowuje informacje czy gra jest uruchomiona
    run=True
    #pozyvje startowe węża
    zmiennaX=300
    zmiennaY=300
    #pozycja startowa jabłka
    jablkoX=random.randint(0,19)*30
    jablkoY=random.randint(0,19)*30
    #liczba punktów
    punkty=0 
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
                    zmiennaX=zmiennaX+30
                elif zdarzenia.key==pygame.K_LEFT:
                    zmiennaX=zmiennaX-30
                elif zdarzenia.key==pygame.K_UP:
                    zmiennaY=zmiennaY-30
                elif zdarzenia.key==pygame.K_DOWN:
                    zmiennaY=zmiennaY+30
                #sprawdzanie krawędzi
                if zmiennaX>=600:
                    zmiennaX=0
                if zmiennaX<0:
                    zmiennaX=600
        #rysowanie węża
        #definiujemy kształ węża
        ksztaltWaz=pygame.Rect((zmiennaX,zmiennaY),(30,30))
        #dodanie kształtu do okienka
        pygame.draw.rect(oknoGry,(100,100,100),ksztaltWaz)
        #zjadanie jabłka
        if zmiennaX==jablkoX and zmiennaY==jablkoY:
                jablkoX=random.randint(0,19)*30
                jablkoY=random.randint(0,19)*30
                punkty+=1 #punkty=punkty+1


        #rysowanie jabłka
        pygame.draw.circle(oknoGry,(255,0,0),(jablkoX+15,jablkoY+15),15)

        #napisy na ekranie
        czcionka=pygame.font.SysFont('arial', 25)
        tekst=czcionka.render("Zdobyłeś punkty: {0}".format(punkty),1,(51,51,255))
        oknoGry.blit(tekst,(10,10))

        #aktualizowanie zawartości okna gry
        pygame.display.update()

#wywołanie funkcji, pozwala na uruchomienie gry
waz()
