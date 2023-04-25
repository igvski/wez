import pygame_menu
import pygame
#import pliku z grą
import waz

def wlaczGre():
    waz.waz()
def main():
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    menu=pygame_menu.Menu("Gra Wąż 3TIE",600,600,theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button('Urochom grę',wlaczGre,background_color=(0,255,0))
    menu.add.selector("Wybierz ilość jabłek",[('jedno',1,)])
    menu.mainloop(oknoGry)

main()