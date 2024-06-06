    
from setting import *
import pygame as pg
import time
from claas_Timer import *
from class_Button import*
class Floor:
    def __init__ (self,number_floor,x,y):
        self.number_floor = number_floor
        self.timer = -2
        self.occupied = True
        self.img = pg.transform.scale (pg.image.load(IMG_BRICK_WALL),IMG_BRICK_WALL_SIZE)
        self.line = pg.transform.scale (pg.image.load(IMG_LINE),(IMG_LINE_SIZE))
        self.x = x
        self.y = y
        self.floor_button=Button(self.number_floor,self.x,self.y)
        self.time = Timer(self.number_floor,self.x,self.y)

    def update_valuos(self,time):
        self.occupied = False
        self.time.set_time (time)
        self.floor_button.color = 1


    def get_Invitation_Button(self,event_pos):
        if self.floor_button.button_erea.collidepoint(event_pos):
            if self.occupied:
              return True
        return False
 
    def plot_floor(self,screen,font,time_past):
        screen.blit(self.img,(self.x,self.y))
        if self.number_floor < FLOOR_NUMBER - 1:
            screen.blit(self.line,(self.x,self.y-IMG_LINE_SIZE[1]))           
        self.floor_button.plot_Button(screen,font)
        self.time.apdet_time(time_past)
        self.time.plot_time(screen,font)
