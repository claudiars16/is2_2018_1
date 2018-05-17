import pygame as pg
import sys
from random import randint
from db.database import Database
from config import *

class Game():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.win = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        self.run()
    
    def run(self):
        pass
    
    def update(self):
        pass
    
    def events(self):
        pass
    
    def draw(self):
        pass
    
    def changeState(self, state):
        pass
    
    
    
    
g = Game()
while g.running:
    g.new()

pg.quit()