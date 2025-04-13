import math
import random
import pygame as pg
from pygame import transform
from Racket import SIZE_X as RACKET_SIZE
from bonus import BONUS, Bonus
from setings import SIZE, X_POS, Y_POS, ANGLE

SPEED = 0.0

class Ball:
    def __init__(self, texture, field: tuple):
        self.circle = pg.Surface((SIZE, SIZE), pg.SRCALPHA)  
        self.rect = self.circle.get_rect(center=(X_POS, Y_POS))
        self.texture = transform.scale(texture, (SIZE, SIZE))
        self.speed = 0.0
        self.angle = math.radians(ANGLE)
        self.field = field
        self.attached = True
        self.bonus_attached = False
        self.metal = False
        self.last_speed = 0.0
        self.pos_on_racket = 0.0

    def move(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)

    def change_angle(self, angle_degrees):
        self.angle = math.radians(angle_degrees)

    def block_hit(self, blocks):
        bonus = "None"
        score = 0
        for block in blocks: 
            if self.rect.colliderect(block.rect) and block.hits > 0: 
                self.speed += 0.1
                score += 10
                if not self.metal:  
                    if abs(self.rect.bottom - block.rect.top) < self.speed:  # Снизу
                        self.angle = -self.angle
                    elif abs(self.rect.top - block.rect.bottom) < self.speed:  # Сверху
                        self.angle = -self.angle
                    elif abs(self.rect.right - block.rect.left) < self.speed:  # Слева
                        self.angle = math.pi - self.angle
                    elif abs(self.rect.left - block.rect.right) < self.speed:  # Справа
                        self.angle = math.pi - self.angle
                block.hit()
                if block.hits <= 0:
                    broke_sound = pg.mixer.Sound("./Sounds/block_broke.mp3")
                    broke_sound.play()
                    if random.randint(0, 5) == 3:
                        bonus_i = random.randint(0,5)
                        bonus_str = BONUS[bonus_i]
                        bonus = Bonus(bonus_str, block.rect)
                break 
        return bonus, score 


    def update(self, racket, racket_size, blocks):
        if self.rect.x <= 0 or self.rect.x + SIZE >= self.field[0]:
            self.angle = math.pi - self.angle
            rebound_sound = pg.mixer.Sound("./Sounds/rebound.mp3")
            rebound_sound.play() 

        if self.rect.y <= 0:
            self.angle = -self.angle
            rebound_sound = pg.mixer.Sound("./Sounds/rebound.mp3")
            rebound_sound.play() 

        if self.rect.colliderect(racket.rect):
            racket_sound = pg.mixer.Sound("./Sounds/racket.mp3")
            if self.bonus_attached:
                self.angle = math.radians(ANGLE)
                if self.speed != 0:
                    racket_sound.play()
                    self.pos_on_racket = self.rect.centerx - racket.rect.centerx
                    self.last_speed = self.speed
                    self.speed = 0.0
            else:
                racket_sound.play()
            hit_pos = float(abs(float(racket.rect.centerx - self.rect.centerx)) / float((racket_size[0]) / 2))  
            if racket.rect.centerx > self.rect.centerx:
                self.angle = math.radians(90) + hit_pos * math.radians(89)
            else:
                self.angle = math.radians(90) - hit_pos * math.radians(89)

        if self.rect.y >= self.field[1]:
            self.speed = 0.0 
            return "Game Over", 0

        bonus, score = self.block_hit(blocks)
        return bonus, score

    def attached_move(self,racket):
        self.rect.x = racket.rect.centerx - SIZE // 2 + self.pos_on_racket

        if self.rect.x < 0.0 - SIZE // 2 + racket.get_size()[0] // 2:
            self.rect.x = racket.get_size()[0] // 2 - SIZE // 2 + self.pos_on_racket
        if self.rect.x + SIZE // 2 + racket.get_size()[0] // 2 > self.field[0]:
            self.rect.x = self.field[0] - SIZE//2 - racket.get_size()[0] // 2 + self.pos_on_racket