import pygame as pg
from config import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, stage):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.stage = stage
        self.image.fill(self.__getSuit())
        self.rect = self.image.get_rect()
        self.rect.center = (25, 300)
        self.pos = vec(25, 300) #POSITION IN ALL STAGE 
        self.pos_screen = vec(25, 300) #POSITION IN SCREEN
        self.vel = vec(0, 0)
        self.a = self.__getAcceleration()
        self.acc = vec(0, 0)
        self.des = 0

    def move(self, side):
        # print("ACC :{}".format(self.acc.x))
        # print("VEL :{}".format(self.vel.x))
        # print("POS :{}".format(self.pos.x))
        
        #DEF GRAVITY
        self.acc = vec(0,PLAYER_GRAV)
        #DEF ACELE
        self.acc.x = self.a * side
        #DEF FRICC
        self.acc.x += self.vel.x * PLAYER_FRIC
        # ECU OF MOVE
        self.vel += self.acc
        m = self.pos.x
        self.pos += self.vel + 0.5 * self.acc
        self.des = round(self.pos.x - m,0)
        
        WHP = self.image.get_width() / 2
        # NO OUT OF STAGE
        if self.pos.x >= self.stage.stageWidth - WHP:
            self.pos.x = self.stage.stageWidth - WHP
            self.stage.loseState = True
            self.stage.game.lose_sound()
        if self.pos.x <= WHP:
            self.pos.x = WHP
        # IN THE MIDDLE OF THE SCREEM
        # CALCULATE HOW MUCH MOVE THE SCREEN
        if self.pos.x < self.stage.startScrollingPosX:
            self.pos_screen.x = self.pos.x
        elif self.pos.x > self.stage.stageWidth - self.stage.startScrollingPosX:
            self.pos_screen.x = self.pos.x - self.stage.stageWidth + WIDTH
        else:
            self.pos_screen.x = self.stage.startScrollingPosX
            self.stage.stagePosX += -self.vel.x
            
        
        self.rect.center = (self.pos_screen.x, self.pos.y-WHP)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.stage.platforms, False)
        hits_floor = pg.sprite.spritecollide(self,self.stage.bases, False)
        self.rect.x -= 1
        if hits or hits_floor:
            self.vel.y = -10      

    def __getSuit(self):
        switcher = {
            1 : GREEN,
            2 : BLUE,
            3 : ORANGE
        }
        return switcher.get(self.stage.game.suit)

    def __getAcceleration(self):
        switcher = {
            1 : PLAYER_ACC_1,
            2 : PLAYER_ACC_2,
            3 : PLAYER_ACC_3
        }
        return switcher.get(self.stage.game.difficulty)

class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self , dis):
        self.rect.x -= dis

class Life(pg.sprite.Sprite):

    def __init__(self , x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../assets/one/life.png")
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self , dis):
        self.rect.x -= dis

class Tumi(pg.sprite.Sprite):

    def __init__(self , x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("../assets/one/tumi.png")
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self , dis):
        self.rect.x -= dis