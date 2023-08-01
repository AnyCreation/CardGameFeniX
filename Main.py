import GameCard as GC
import ListCard as LC
import pygame
import random

w, h = 1200, 900
dis = pygame.display.set_mode((w, h))

AW = (w / 2, h / 2)
S = False
M = False

""" Create Power and Attact for Cards """
Keys = LC.Cards.keys()
Cards = LC.Cards[list(Keys)[random.randint(0, len(Keys) - 1)]]
Attact, power = Cards[random.randint(0, len(Cards) - 1)]

""" Inventory """
Limit_has_Cards = [0, 0, 0]
Cards_In_Place = []

while True:
    dis.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            S = True
        elif event.type == pygame.MOUSEBUTTONUP:
            S = False



    pygame.display.update()
