import pygame as pg

SIZE_X = 200
SIZE_Y = 20

class Racket:
    def __init__(self, field: tuple):
        self.paddle = pg.Surface((SIZE_X, SIZE_Y), pg.SRCALPHA)
        self.rect = self.paddle.get_rect(center=(field[0] / 2, field[1] - SIZE_Y))
        self.field_width = field[0]

    def update(self, mouse_pos: tuple):
        self.rect.x = mouse_pos[0] - self.rect.size[0] // 2 

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.size[0] > self.field_width:
            self.rect.x = self.field_width - self.rect.size[0]

    def get_size(self):
        return self.rect.size
    
    def set_size(self, new_width, new_height):
        self.paddle = pg.Surface((new_width, new_height), pg.SRCALPHA)

        center_x = self.rect.centerx
        bottom_y = self.rect.bottom - SIZE_Y // 2

        self.rect = self.paddle.get_rect(center=(center_x, bottom_y))

