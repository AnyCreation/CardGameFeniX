import pygame

pygame.font.init()


class Card:

    def __init__(self, WINDOW, MINA, CENTER, AIN_EDIT, POSMOUSE):
        self.WINDOW = WINDOW
        self.x, self.y = CENTER
        self.AIN_EDIT = AIN_EDIT

        self.w = 120 / MINA
        self.h = 170 / MINA
        self.col = 8

        self.Down = pygame.Rect(self.x - (self.w / 2), self.y - (self.h / 2), self.w, self.h)

        self.Up_Attact = pygame.Rect((self.x - (self.w / 2)) + self.col, (self.y - (self.h / 2)) + self.col - 1,
                                     self.w - self.col * 2, (self.h - self.col * 2) // 2)

        self.Up_Power = pygame.Rect((self.x - (self.w / 2)) + self.col,
                                    (self.y - (self.h / 2)) + self.col + (self.h - self.col * 2) // 2 + 1,
                                    self.w - self.col * 2, (self.h - self.col * 2) // 2)

        self.POSMOUSE = POSMOUSE
        self.MOUSE_RECT = pygame.Rect(self.POSMOUSE[0], self.POSMOUSE[1],
                                      50, 50)

    @classmethod
    def Text(cls, text, RECT):  # Just make a text!!!!!!
        SIZE = 30
        font = pygame.font.Font('Fo/ofont.ru_EE-Bellflower.ttf', SIZE)
        text = font.render(text, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = RECT.center
        return text, textRect, SIZE

    @classmethod
    def LimitText(cls, text):  # If text too long!!!!!!
        X = list(text)
        M = ''
        for i in range(3):
            M += X[i]

        M += '.'
        return M

    @classmethod
    def INFO(cls, RECT_CARD, MOUSEPOS):  # Info of the power!!!!!!
        X = RECT_CARD[0] <= MOUSEPOS[0] <= RECT_CARD[0] + RECT_CARD[2]
        Y = RECT_CARD[1] <= MOUSEPOS[1] <= RECT_CARD[1] + RECT_CARD[3]

        return X, Y

    def Update(self):
        pygame.draw.rect(self.WINDOW, (184, 184, 184), self.Down)
        pygame.draw.rect(self.WINDOW, (164, 164, 164), self.Up_Attact)
        pygame.draw.rect(self.WINDOW, (164, 164, 164), (self.Up_Power[0], self.Up_Power[1],
                                                        self.Up_Power[2], self.Up_Power[3]))

        TEXT_UP = self.Text(str(self.AIN_EDIT[0]), self.Up_Attact)
        self.WINDOW.blit(TEXT_UP[0], TEXT_UP[1])
        TEXT_DOWN = self.Text(str(self.LimitText(self.AIN_EDIT[1])), self.Up_Power)
        self.WINDOW.blit(TEXT_DOWN[0], TEXT_DOWN[1])

        INF_POWER_CARD = self.INFO(self.Up_Power, self.POSMOUSE)

        if INF_POWER_CARD[1] and INF_POWER_CARD[0]:
            INFO_RECT = self.Text(str(self.AIN_EDIT[1]), self.MOUSE_RECT)
            self.Text(self.AIN_EDIT[1], self.WINDOW.blit(INFO_RECT[0], INFO_RECT[1]))