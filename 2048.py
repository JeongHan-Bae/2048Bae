# MIT License

"""Copyright (c) 2023 JeongHan-Bae

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
from Biblio2048 import *
import pygame
import time
import sys

pygame.init()
# init
ecran = 510
fenetre = pygame.display.set_mode((ecran, ecran + 45))
fenetre.fill((55, 55, 58))
# fenêtre
pygame.display.set_caption("2048 JeongHan-Bae")
# titre
IMGN = pygame.transform.scale(pygame.image.load("images/GN.jpg"), (ecran, ecran))
IMPD = pygame.transform.scale(pygame.image.load("images/PD.jpg"), (ecran, ecran))
ModeChoix = pygame.transform.scale(pygame.image.load("images/ModeChoix.jpg"), (ecran, ecran))
# images
font = pygame.font.SysFont("Courier New", 22, bold=True, italic=False)  # Police
Mode_1 = font.render("Mode 1 : 4*4", True, (255, 255, 255))
Mode_2 = font.render("Mode 2 : 5*5", True, (255, 255, 255))
Choix = font.render("Choisissez le Mode Vous Préférez", True, (255, 255, 255))
Re = font.render("Appuyez sur Espace pour Recommencer", True, (255, 255, 255))


# phrases
def Affichage():
    for i in range(0, len(Base.arraylist)):
        for j in range(0, len(Base.arraylist[0])):
            Im = pygame.transform.scale(pygame.image.load("images/" + str(Base.arraylist[j][i]) + ".jpg"),
                                        (((ecran - 10) / dim) - 10, ((ecran - 10) / dim) - 10))
            fenetre.blit(Im, ((10 + i * ((ecran - 10) / dim)), 10 + j * ((ecran - 10) / dim)))
    # ajouter les objets
    pygame.display.update()


fenetre.blit(ModeChoix, (0, 0))
fenetre.blit(Choix, (30, ecran + 5))
pygame.display.flip()
# affichage à la 1 ère fois
Arret = False
Progres = None
while not Arret:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and Progres == False:
            if event.key == pygame.K_SPACE:
                fenetre.fill((55, 55, 58))
                fenetre.blit(ModeChoix, (0, 0))
                fenetre.blit(Choix, (30, ecran + 5))
                Progres = None
                pygame.display.update()
        if event.type == pygame.KEYDOWN and Progres == None:
            if event.key == pygame.K_a:
                dim = 4
                Base = array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]])
                # Base
                Progres = True
                But = 11
                fenetre.fill((55, 55, 58))
                fenetre.blit(Mode_1, (60, ecran + 5))
                Base.Neuf()
                Affichage()
            elif event.key == pygame.K_b:
                dim = 5
                Base = array([[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])
                # Base
                Progres = True
                But = 13
                fenetre.fill((55, 55, 58))
                fenetre.blit(Mode_2, (60, ecran + 5))
                Base.Neuf()
                Affichage()
        if event.type == pygame.QUIT:
            Arret = True
            sys.exit()
        elif event.type == pygame.KEYDOWN and Progres == True:
            # distinguer touche de clavier utilisée
            if event.key == pygame.K_LEFT:
                if Base.Acces_g():
                    Base.gauche()
                    Affichage()
                    time.sleep(0.1)
                    Base.Neuf()
                    Affichage()
            elif event.key == pygame.K_RIGHT:
                if Base.Acces_d():
                    Base.droite()
                    Affichage()
                    time.sleep(0.1)
                    Base.Neuf()
                    Affichage()
            elif event.key == pygame.K_UP:
                if Base.Acces_h():
                    Base.haut()
                    Affichage()
                    time.sleep(0.1)
                    Base.Neuf()
                    Affichage()
            elif event.key == pygame.K_DOWN:
                if Base.Acces_b():
                    Base.bas()
                    Affichage()
                    time.sleep(0.1)
                    Base.Neuf()
                    Affichage()
            if Base.Mort():
                fenetre.fill((55, 55, 58))
                Affichage()
                Progres = False
                fenetre.blit(Re, (30, ecran + 5))
                time.sleep(0.5)
                IMPD.set_alpha(200)
                fenetre.blit(IMPD, (0, 0))
                pygame.display.update()
            if Base.Gagne(But):
                fenetre.fill((55, 55, 58))
                Affichage()
                Progres = False
                fenetre.blit(Re, (30, ecran + 5))
                time.sleep(0.5)
                IMGN.set_alpha(210)
                fenetre.blit(IMGN, (0, 0))
                pygame.display.update()
        # conditions
