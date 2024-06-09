from setting import *
import pygame as pg
import time
from elements import *

    
class Button:
    
    def __init__ (self,number_floor,x,y):
        self.color=0
        self.number_floor=number_floor
        self.x = x + BUTTON_LOCATION [0]
        self.y = y + BUTTON_LOCATION [1]
        self.img_green = pg.transform.scale (pg.image.load(IMG_BOTTON_GREEN),IMG_BOTTON_SIZE)
        self.img_gray = pg.transform.scale (pg.image.load(IMG_BOTTON_GRAEY),IMG_BOTTON_SIZE)
        self.arr=[self.img_gray,self.img_green]
        self.button_erea = pg.Rect(self.x - BUTTON_EREA[0], self.y - BUTTON_EREA[1] ,BUTTON_SIZE[0] + (BUTTON_EREA[0]*2), BUTTON_SIZE[1] + BUTTON_EREA[1])
        pg.mixer.init()
        self.ding =pg.mixer.Sound(DING)
    
    def exchange_color_to_grae_and_Sound_ding(self):
        if self.color == 1:
            self.color = 0
            pg.mixer.Sound.play(self.ding)


            
        
        
        

    def Button_is_green(self):
        return bool(self.color)


    def plot_Button(self,screen,font):
        img_i = self.arr[ self.color]
        screen.blit((img_i),(self.x,self.y))
        screen.blit(font.render(str(self.number_floor),True,(0,0,0)),(self.x + NUMBER_FLOOR_LOCATION[0],self.y + NUMBER_FLOOR_LOCATION[1]))
