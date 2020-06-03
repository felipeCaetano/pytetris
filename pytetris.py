from random import randint

import pygame
from pytetris.pytetris.blocos import Blocos
from pytetris.pytetris.game_constants import DISPLAY_WIDTH, DISPLAY_HEIGTH, MAX_NUM_BLOCS, FRAME_RATE, LEVEL

pygame.init()


class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
        pygame.display.set_caption("PyTetris")
        self.blocs_area = pygame.image.load('imagens/fundo.png').convert_alpha()
        self.background = pygame.image.load('imagens/background.jpg')
        self.grid = pygame.image.load('imagens/fundo.png').convert_alpha()
        self.preview_area = pygame.Surface((95, 95))
        self.clock = pygame.time.Clock()
        self.bloco = self.get_bloco()
        self.next_bloco = self.get_bloco()
        self.score = 0

    def play(self):
        running = True
        # self.create_game_area()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.bloco.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.bloco.move_left()
                    elif event.key == pygame.K_UP:
                        self.bloco.rotate()
                    elif event.key == pygame.K_DOWN:
                        self.bloco.gravity(LEVEL)
                    elif event.key == pygame.K_SPACE:
                        self.bloco.place()
                        self.bloco, self.next_bloco = self.next_bloco, self.get_bloco()
                    elif event.key == pygame.K_p:
                        self._pause()
                    elif event.key == pygame.K_q:
                        running = False
            self.preview_area.fill((0, 0, 0))
            self.preview_area.blit(self.next_bloco.image,
                                   [(47 - self.next_bloco.width // 2),
                                    (47 - self.next_bloco.heigth // 2)])
            self.display_surface.blit(self.background, (0, 0))
            self.display_surface.blit(self.blocs_area, [1, 50])
            self.draw_bloco(self.bloco)
            self.bloco.gravity(.1)
            self.display_surface.blit(self.preview_area, [360, 55])
            self.clock.tick(FRAME_RATE)
            pygame.display.flip()

    def create_game_area(self):
        self.display_surface.blit(self.background, [0, 0])
        pygame.draw.rect(self.preview_area, (24, 255, 24), (0, 0, 90, 90), 3)
        self.display_surface.blit(self.preview_area, [360, 55])
        self.display_surface.blit(self.blocs_area, [0, 50])
        copia = self.blocs_area.copy()

    def get_blocos(self):
        len_blocos = len(self.blocos) - 1
        return self.blocos[randint(0, len_blocos)], self.blocos[randint(0, len_blocos)]

    def _pause(self):
        pass

    def get_bloco(self):
        num_bloco = randint(0, MAX_NUM_BLOCS)
        return Blocos(num_bloco)

    def draw_bloco(self, bloco):
            self.display_surface.blit(bloco.image, (bloco.x, bloco.y))


if __name__ == '__main__':
    game = Game()
    game.create_game_area()
    game.play()
