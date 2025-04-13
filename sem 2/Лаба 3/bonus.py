from pygame import transform, image
import pygame as pg
from Racket import SIZE_X, SIZE_Y, Racket
from setings import DEFOULT_SPEED, FIELD, HEIGHT, TEXTURE_PATH, WIDTH
BONUS = [
    'speed_up', 'speed_down', 'metal_ball', 'ball_attached',
    'racket_up', 'racket_down',
    'block_explosive',
    'health_up', 'death', 'next_level'
]
class Bonus:
    def __init__(self, name, rect : tuple):
        self.speed = DEFOULT_SPEED // 1.5
        self.name = name
        texture = image.load(f"{TEXTURE_PATH}Bonuses/{name}.png").convert_alpha()
        self.texture = transform.scale(texture, (WIDTH , HEIGHT))
        self.rect = rect

    def impact(self):
        if self.name == BONUS[0]:
            self.device.speed += DEFOULT_SPEED
        if self.name == BONUS[1]:
            self.device.speed *= 0.6
        if self.name == BONUS[2]:
            self.device.damage = 4
            self.device.metal = True
        if self.name == BONUS[3]:
            self.device.bonus_attached = True 
        if self.name == BONUS[4]:
            self.device.set_size(1.5 * SIZE_X, SIZE_Y)
        if self.name == BONUS[5]:
            self.device.set_size(0.6 * SIZE_X, SIZE_Y)

    def add_device(self, ball, racket, blocks):
        if self.name in BONUS[0:4]:
            self.device = ball
        if self.name in BONUS[4:6]:
            self.device = racket
        if self.name in BONUS[6]:
            self.device = blocks

    def drop(self, ball, racket, block):
        if self.rect[1] < FIELD[1]:
            self.rect[1] += self.speed
        else:
            self.rect[1] = FIELD[1]
        if racket.rect.colliderect(self.rect):
            self.add_device(ball, racket, block)
            self.impact()
            self.name = "None"
            return True
