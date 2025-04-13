from pygame import  init, quit
import pygame as pg
from Ball import Ball
from Racket import Racket
from game import Game
from level import create_blocks, levels
from setings import FIELD, TEXTURE_PATH

init()
screen = pg.display.set_mode(FIELD)
clock = pg.time.Clock()
try:
    ball_texture = pg.image.load(f"{TEXTURE_PATH}ball.png").convert_alpha()
except FileNotFoundError:
    print("Текстура не найдена, использую стандартный цвет")
game = Game()
while game.health > 0:
    ball = Ball(ball_texture, FIELD)
    racket = Racket(FIELD)
    game.add_ball_and_racket(ball,racket)
    blocks = create_blocks(levels[game.finished_levels])
    result = game.level(screen, clock, blocks)
    while result == "Game Over":
        ball = Ball(ball_texture, FIELD)
        racket = Racket(FIELD)
        game.add_ball_and_racket(ball,racket) 
        result = game.level(screen, clock, blocks)
quit()