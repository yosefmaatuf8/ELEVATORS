import pygame as pg
import time
from setting import *
import math
from class_Bulding import *
from class_elevator import *
class manager:  # responsible for connection between the classes floor and elevatrs
    def __init__(self) -> None:
        self.Building = Building()
        self.elevators = Elevator_sistem(self.Building.Floors[0])
        self.last_time = time.time()
        self.current_time=0
        self.time_past = 0
        self.background = pg.transform.scale (pg.image.load(IMG_SKY_BACKGROUND),(WINDOW_X,WINDOW_Y))

    def timer (self):
        self.current_time=time.time()
        time_past = self.current_time - self.last_time
        self.last_time = time.time()
        self.time_past = time_past
            
    def user_get_click(self,event_pos):
        for floor_loop in self.Building.Floors:
            if floor_loop.get_Invitation_Button(event_pos):
               elevator_near= self.elevators.chose_elevator(floor_loop)
               floor_loop.update_valuos(elevator_near)


    def plot_manager(self,screen,font):
        self.timer()
        screen.blit(self.background,(0,0))
        self.Building.plot_Bulding(screen,font,self.time_past)
        self.elevators.plot_all_elevators(screen,self.time_past)
    
               


