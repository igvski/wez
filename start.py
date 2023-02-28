#pobranie biblioteki pygame
import pygame

#utworzenie funkcji waz
def waz():
    #inicjalizacja biblioteki
    pygame.init()
    #utworzenie okna gry i określenie jej rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną, która przechowuje informacje czy gra jest uruchomiona
    run=True
    #pętla while sprawdza czy warunek zmiennej run jest prawdziwy, jak jest nieprawdziwy kończy swoje działanie
    while(run):
        #wypełnienie okna kolorem
        oknoGry.fill((0,0,0))
        #ustawienie opóźnienia odświeżania gry
        pygame.time.delay(200)
        #sprawdzanie czy istnieją jakieś zdarzenia i zapisanie ich do zmiennej "zdarzenia"
        for zdarzenia in pygame.event.get():
            #jeżeli zmienna "zdarzenia" przechowuje naciśnięcie przycisku zamknij to zmieniamy wartość zmiennej "run"
            if zdarzenia.type==pygame.QUIT:
                run=False
        #rysowanie węża
        #definiujemy kształt węża
        ksztaltWaz=pygame.Rect((300,300),(15,15))
        #dodanie kształtu do okienka
        pygame.draw.rect(oknoGry,(100,100,100),ksztaltWaz)
        #aktualizowanie zawartości okna gry
        pygame.display.update()

#wywołanie funkcji, pozwala na uruchomienie gry
waz()

