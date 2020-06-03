import pygame

from pytetris.pytetris.game_constants import DISPLAY_WIDTH, DISPLAY_HEIGTH, X_TILE, Y_TILE

images = [
    'imagens/cube01.png',
    'imagens/cube02.png',
    'imagens/cube03.png',
    'imagens/cube04.png',
    'imagens/cube05.png'
]
class Blocos:
    def __init__(self, bloc_num):
        self.bloc_num = bloc_num
        self.load_image(images[bloc_num])
        self.choose_bloc(bloc_num)
        self.x = DISPLAY_WIDTH / 2 - self.width - 10
        self.y = 28
        self.forma = []
        self.rot = 0

    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.width = self.image.get_width()
        self.heigth = self.image.get_height()

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.rot += 1
        if self.rot > 3:
            self.rot = 0

    def choose_bloc(self, bloc_num):
        if bloc_num == 1:
            self.forma = ['8888', 'F000', '8888', 'F000']
            self.rot = 0

        elif bloc_num == 2:
            self.forma = ['CC00', 'CC00', 'CC00', 'CC00']
            self.rot = 0

        elif bloc_num == 3:
            self.forma = ['E800', 'C440', '2E00', '88C0']
            self.rot = 0

        elif bloc_num == 4:
            self.forma = ['4C40', '4E00', '8C80', 'E400']
            self.rot = 0

        elif bloc_num == 5:
            self.forma = ['C600', '4C80', 'C600', '4C80']
            self.rot = 0

    def convert_form(self):
        converted_form = []
        for form in self.forma[self.rot]:
            x = int(form, 16)
            y = [int(z) for z in format(x, '04b')]
            converted_form.append(y)
        return converted_form

    def gravity(self, level):
        self.y += level*Y_TILE
        if self.y + self.heigth > DISPLAY_HEIGTH:
            self.y = DISPLAY_HEIGTH - self.heigth

    def move_left(self):
        self.x -= X_TILE / 2
        if self.x < 0:
            self.x = 1

    def place(self):
        self.y = DISPLAY_HEIGTH - self.heigth

    def isplaced(self):
        if self.y == DISPLAY_HEIGTH - self.heigth:
            return True
        return False

    def move_right(self):
        self.x += X_TILE / 2
        if self.x > DISPLAY_WIDTH - 95 - 55:
            self.x = DISPLAY_WIDTH - 95 - 55

