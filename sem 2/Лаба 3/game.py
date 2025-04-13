import pygame as pg
import sys
from Ball import SPEED, Ball
from Racket import Racket
from bonus import Bonus
from setings import DEFOULT_SPEED, FIELD, HEALTH_HEIGHT, HEALTH_WEIGHT, SCORE_POS, TEXTURE_PATH

class Game:
    def __init__(self):
        self.health = 3
        self.finished_levels = 0
        texture = pg.image.load(f"{TEXTURE_PATH}Health.png").convert_alpha()
        self.health_texture = pg.transform.scale(texture, (HEALTH_WEIGHT, HEALTH_HEIGHT))
        self.score = 0
        self.score_add_health = 0
        self.pause = False

    def add_ball_and_racket(self, ball: Ball, racket : Racket):
        self.ball = ball
        self.racket = racket

    def event_handler(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
                sys.exit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE and self.ball.attached:
                    self.ball.speed = DEFOULT_SPEED
                    self.ball.attached = False

                if e.key == pg.K_SPACE and self.ball.bonus_attached:
                    self.ball.speed = self.ball.last_speed
                    self.ball.rect.y -= self.ball.speed

                if e.key == pg.K_ESCAPE:
                    self.pause = not self.pause
                else:
                    self.pause = False

            if e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1 and self.ball.attached:
                    self.ball.speed = DEFOULT_SPEED
                    self.ball.attached = False

                if e.button == 1 and self.ball.bonus_attached:
                    self.ball.speed = self.ball.last_speed
                    self.ball.rect.y -= self.ball.speed
            if e.type == pg.MOUSEMOTION:
                self.racket.update(pg.mouse.get_pos())
                if (self.ball.attached or self.ball.bonus_attached) and self.ball.speed == 0:
                    self.ball.attached_move(self.racket)
                

    def level(self, screen : pg.display, clock, blocks):
        self.run = True
        bonuses = []
        while self.run:
            self.event_handler()
            if not self.pause:

                block_quantity = 0
                if self.score - self.score_add_health >= 10000: #Нужное кол-во опыта для доп. жизни
                    self.score_add_health += 10000
                    self.health +=1

                result, score = self.ball.update(self.racket, self.racket.get_size(), blocks)
                if result:
                    if result == "Game Over":
                        self.health -= 1
                        fail_sound = pg.mixer.Sound("./Sounds/fail.ogg")
                        fail_sound.play() 

                        return "Game Over"
                    else:
                        self.score += score
                        if result != "None":
                            bonuses.insert(0, result)

                for bonus in bonuses:
                    if bonus:
                        bonus.drop(self.ball, self.racket, blocks)
                        if bonus.name == "None":
                            self.score += 100
                            bonuses.remove(bonus)
                self.ball.move()
                font = pg.font.SysFont('arial', 32)
                text = font.render(str(self.score),True, (0,0,0))

            screen.fill((255, 255, 255))
            for block in blocks:
                if block.hits >0:
                    screen.blit(block.texture, (block.rect.x, block.rect.y))
                    block_quantity+= 1
            
            for bonus in bonuses:
                if bonus and bonus.name != "None":
                    screen.blit(bonus.texture, bonus.rect)
            screen.blit(self.ball.texture, self.ball.rect)
            pg.draw.rect(screen, (50, 50, 255), self.racket.rect)
            screen.blit(text, SCORE_POS)
            for i in range(self.health):
                screen.blit(self.health_texture, (FIELD[0]- (45 * (i+1)), 30))
            pg.display.flip()

            clock.tick(120)
            if block_quantity == 0:
                self.finished_levels +=1
                self.score+= 1000
                return