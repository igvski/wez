import pygame_menu
import pygame
import wazz
import jablko

rozdzielczosc = (600, 600)

def wlacz_gre():
    print(rozdzielczosc)
    wazz.waz(rozdzielczosc)

def zmienJablka(tekst, ilosc):
    wazz.iloscJablek = ilosc

def zmienKolorWaz1(kolor):
    wazz.ustawKolorWaz1(kolor)

def zmienKolorWaz2(kolor):
    wazz.ustawKolorWaz2(kolor)

def zmienRozmiar(x, rozmiar):
    wazz.rozmiarOkna = rozmiar

def main():
    pygame.init()
    oknoGry=pygame.display.set_mode((600,600),0,32)
    pygame.display.set_caption("Gra Wąż")
    menu = pygame_menu.Menu("Gra wąż 3TIE", 600, 600, theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button("Uruchom grę", wlacz_gre, background_color = (0,0,0))
    menu.add.selector("Ilość jabłek", [("jedno", 1), ("dwa", 2), ("pięć", 5), ("dziesięć", 10), ("dwadzieścia", 20)], onchange=zmienJablka)   
    menu.add.color_input("Kolor gracza 1: ", "rgb", default=(100,100,100), onreturn=zmienKolorWaz1)
    menu.add.color_input("Kolor gracza 1: ", "rgb", default=(100,100,100), onreturn=zmienKolorWaz2)
    menu.add.selector("Wybierz rozmiar okna: ", [("600x600", (600,600)), ("900x600", (900,600)), ("900x900", (900,900)), ("1200x900", (1200,900))], onchange=zmienRozmiar)

    menu.mainloop(oknoGry)

main()