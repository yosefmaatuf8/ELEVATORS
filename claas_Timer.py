
from setting import *
import pygame as pg
import time
class Timer:

    def __init__(self,Which_flor,Which_flor_x,Which_flor_y) -> None:
        self.time=-2 
        self.x=Which_flor_x
        self.y=Which_flor_y  


    def set_time(self,value):
        self. time = value


    def apdet_time(self,time_past):
        if self.time > -2:
                self.time -= time_past


    def get_time(self):
         if self.time <= -2:
            time_i = 0 
         elif self.time >= 0:
            time_i= self.time +2
         else:
            time_i = 2 - abs (self.time)
         return time_i


    def plot_time(self,screen,font):
        if self.time >= 0: 
            screen.blit(font.render(str(round( self.time,1)),True,(0,0,0)),(self.x+IMG_BRICK_WALL_SIZE[0],self.y+TIMER_LOCATION_Y))
