import GameCard as GC
import pygame

w, h = 1200, 900
dis = pygame.display.set_mode((w, h))

AW = (w / 2, h / 2)
S = False


ZONE = pygame.Rect(100, 100, 120, 170)

while True:
    dis.fill('white')
    C = GC.Card(dis, 1, AW, [Attact, power], pygame.mouse.get_pos())
    
    C.Update()
    Me = C.Output_Signal_Of_The_Move()

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
            if Me[0] and Me[1]:
                S = True
        elif event.type == pygame.MOUSEBUTTONUP:
            S = False

    pygame.display.update()
