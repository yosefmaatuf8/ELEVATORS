import pygame as pg
import time
from setting import *
import math

class Building:
    def __init__(self):
        self.Floors=[]
        self.initialize_floors()

    def initialize_floors(self):
        x=LEFT_SPACE
        y=WINDOW_Y-BOTTOM_SPACE  
        for i in range(FLOOR_NUMBER):
           self. Floors.append(Floor(i,x,y))
           y -= FLOOR_SIZE[1]
    def plot_Bulding (self,screen,font,time_past):
        for floor_loop in self.Floors:
             floor_loop.plot_floor(screen,font,time_past)      
            
    
    
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
        screen.blit(self.line,(self.x,self.y-IMG_LINE_SIZE[1]))           
        self.floor_button.plot_Button(screen,font)
        self.time.apdet_time(time_past)
        self.time.plot_time(screen,font)
        
    
class Button:
    
    def __init__ (self,number_floor,x,y):
        self.color=0
        self.number_floor=number_floor
        self.x= x + BUTTON_LOCATION [0]
        self.y=y + BUTTON_LOCATION [1]
        self.img_green=pg.transform.scale (pg.image.load('/home/mefathim/Downloads/green_button.png'),IMG_BOTTON_SIZE)
        self.img_gray=pg.transform.scale (pg.image.load('/home/mefathim/Downloads/grey_button.png'),IMG_BOTTON_SIZE)
        self.arr=[self.img_gray,self.img_green]
        self.button_erea = pg.Rect(self.x - BUTTON_EREA[0], self.y - BUTTON_EREA[1] ,BUTTON_SIZE[0] + (BUTTON_EREA[0]*2), BUTTON_SIZE[1] + BUTTON_EREA[1])
        pg.mixer.init()
        self.ding =pg.mixer.Sound(DING)
    
    def exchange_color(self):
        if self.color == 1:
            self.color = 0
            pg.mixer.Sound.play(self.ding)


            
        
        
        

    def Button_is_green(self):
        return bool(self.color)


    def plot_Button(self,screen,font):
        img_i =self.arr[ self.color]
        screen.blit((img_i),(self.x,self.y))
        screen.blit(font.render(str(self.number_floor),True,(0,0,0)),(self.x + NUMBER_FLOOR_LOCATION[0],self.y + NUMBER_FLOOR_LOCATION[1]))


        
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
        

