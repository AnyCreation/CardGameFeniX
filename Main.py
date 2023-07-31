import GameCard as GC
import pygame
import random

w, h = 1200, 900
dis = pygame.display.set_mode((w, h))

POWER_LIST = ["Кровотечение", "Отравление"]

W = []
for Row in range(2):
    Line = []
    for Coll in range(4):
        Line.append([])
    W.append(Line)


AW = (w / 2, h / 2)
Attact = random.randint(1, 9)
power = POWER_LIST[random.randint(1, len(POWER_LIST) - 1)]
S = False


ZONE = pygame.Rect(100, 100, 120, 170)

while True:
    dis.fill('white')
    C = GC.Card(dis, 1, AW, [Attact, power], pygame.mouse.get_pos())
    
    C.Update()

    pygame.draw.rect(dis, (0, 0, 0), ZONE, 2)

    is_hit = pygame.Rect.colliderect(ZONE, C.Down)
    if is_hit:
        print(C.AIN_EDIT)

    if S:
        AW = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            S = True
        if event.type == pygame.MOUSEBUTTONUP:
            S = False

    pygame.display.update()