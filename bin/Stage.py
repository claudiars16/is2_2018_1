import pygame as pg
import sys
from Component import Component
from db.database import Database
from config import *

class MenuStage():

    def __init__(self, game , win):
        self.database = Database()
        self.game = game
        self.win = win
        self.arrayComponente = []
        self.play = Component(win,pg.image.load("../assets/menu/btn_play.png"),
                                        pg.image.load("../assets/menu/btn_alt_play.png"), 518,450,1)
        self.options = Component(win,pg.image.load("../assets/menu/btn_options.png"),
                                        pg.image.load("../assets/menu/btn_alt_options.png"), 518,550, 1)
        self.exit = Component(win,pg.image.load("../assets/menu/btn_exit.png"),
                                        pg.image.load("../assets/menu/btn_alt_exit.png"), 518,650,1)
        self.__loadComponents(win)
        
    def draw(self):
        for component in self.arrayComponente:
            component.draw()
            component.hover()

    def events(self):
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.exit.inside(mouse[0],mouse[1]):
                    pg.quit()
                    sys.exit()
                if self.options.inside(mouse[0],mouse[1]):
                    self.game.click_sound()
                    self.goOptions()
                if self.play.inside(mouse[0],mouse[1]):
                    self.game.click_sound()
                    self.goNivelOne()

    def update(self):
        pass

    def goOptions(self):
        pass

    def goMenu(self):
        pass
    
    def goNivelOne(self):
        pass

    def __loadComponents(self, win):
        self.arrayComponente.append(Component(win,pg.image.load("../assets/menu/bg.jpg") ,None, 0,0 ,0))
        self.arrayComponente.append(Component(win,pg.image.load("../assets/menu/logo.png"),None, 300,50, 0))
        self.arrayComponente.append(self.play)
        self.arrayComponente.append(self.options)
        self.arrayComponente.append(self.exit)
