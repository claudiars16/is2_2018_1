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
        self.game.changeState(OptionStage(self.game, self.win))

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

class OptionStage():

    def __init__(self, game, win):
        self.database = Database()
        self.game = game
        self.win = win
        self.arrayComponente = []
        self.arraySuit = []
        self.arrayDifficulty = []
        self.suit_a = Component(win,pg.image.load("../assets/options/suit_a.png") ,
                                                pg.image.load("../assets/options/suit_a_press.png"), 400,151 ,1)
        self.suit_b =  Component(win,pg.image.load("../assets/options/suit_b.png") ,
                                                pg.image.load("../assets/options/suit_b_press.png"), 550,151 ,1)                                       
        self.suit_c = Component(win,pg.image.load("../assets/options/suit_c.png") ,
                                                pg.image.load("../assets/options/suit_c_press.png"), 700,151 ,1)
        self.difficulty_1 = Component(win,pg.image.load("../assets/options/level_1.png") ,
                                                pg.image.load("../assets/options/level_1_press.png"), 400,402 ,1)
        self.difficulty_2 = Component(win,pg.image.load("../assets/options/level_2.png") ,
                                                pg.image.load("../assets/options/level_2_press.png"), 550,402 ,1)
        self.difficulty_3 = Component(win,pg.image.load("../assets/options/level_3.png") ,
                                                pg.image.load("../assets/options/level_3_press.png"), 700,402 ,1)
        self.music = Component(win,pg.image.load("../assets/options/music_on.png") ,
                                                pg.image.load("../assets/options/music_off.png"), 475,653 ,1)
        self.sound = Component(win,pg.image.load("../assets/options/sound_on.png") ,
                                                pg.image.load("../assets/options/sound_off.png"), 625,653 ,1)
        self.back = Component(win,pg.image.load("../assets/options/back.png") ,None, 25,25 ,0)
        
        self.creditos = Component(win,pg.image.load("../assets/options/creditos.png") ,None, 1075,675 ,0)

        self.__loadComponents(win)
        self.__init_componets()
        
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
                if self.back.inside(mouse[0],mouse[1]):
                    self.game.click_sound()
                    self.goMenu()
                if self.sound.inside(mouse[0],mouse[1]):
                    self.game.click_sound()
                    self.game.sound = 1 - self.game.sound 
                    self.database.update("sound",self.game.sound)
                    self.sound.active(1-self.game.sound)
                if self.music.inside(mouse[0],mouse[1]):
                    self.game.click_sound()
                    self.game.music = 1 - self.game.music 
                    self.database.update("music",self.game.music)
                    self.music.active(1-self.game.music)
                    if self.game.music == 1:
                        pg.mixer.music.play()
                    else:
                        pg.mixer.music.pause()
    
    def update(self):
        pass

    def goOptions(self):
        pass
    
    def goMenu(self):
        self.game.changeState(MenuStage(self.game, self.win))
    
    def goCreditos(self):
        pass

    def __loadComponents(self,win):
        self.arrayComponente.append(Component(win,pg.image.load("../assets/options/bg.jpg") ,None, 0,0 ,0))
        self.arrayComponente.append(Component(win,pg.image.load("../assets/options/select_suit.png") ,None, 322,41 ,0))
        self.arraySuit.append(self.suit_a)
        self.arraySuit.append(self.suit_b)
        self.arraySuit.append(self.suit_c)
        self.arrayComponente = self.arrayComponente + self.arraySuit
        self.arrayComponente.append(Component(win,pg.image.load("../assets/options/select_level.png") ,None, 322,292 ,0))
        self.arrayDifficulty.append(self.difficulty_1)
        self.arrayDifficulty.append(self.difficulty_2)
        self.arrayDifficulty.append(self.difficulty_3)
        self.arrayComponente = self.arrayComponente + self.arrayDifficulty
        self.arrayComponente.append(Component(win,pg.image.load("../assets/options/select_sound.png") ,None, 431,543 ,0))
        self.arrayComponente.append(self.music)
        self.arrayComponente.append(self.sound)

        self.arrayComponente.append(self.back)
        self.arrayComponente.append(self.creditos)

    def __init_componets(self):
            self.arraySuit[self.game.suit-1].active(True)
            self.arrayDifficulty[self.game.difficulty-1].active(True)
            self.sound.active(1-self.game.sound)
            self.music.active(1-self.game.music)
        
    def __active_group(self, group, element, property):
        element.active(True)
        index = group.index(element)
        setattr(self.game, property, index + 1)
        self.database.update(property, index+1)
        for component in group:
            if group.index(component) != index :
                component.active(False)
