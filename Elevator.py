import pygame as pg
import time
from setting import *       
from estate import *



            
class Elevator:
    def __init__(self,floor_0,x,y) -> None:
        self.Q = []    
        self.location = floor_0
        self.x = x
        self.y= y
        self.img_Elevator= pg.transform.scale (pg.image.load(IMG_ELEVATOR),(IMG_ELEVATOR_SIZE))


    def add_call_Elevator(self,floor):
        """Adds the floor to the queue of the selected elevator"""
        self.Q.append(floor)


    def move_elevator (self,time_past):
          """Updates  y coordinates of the elevator towards its destination
            based on the elapsed time."""
          if self.y + time_past * MOVE_ELEVATOR < self.location.y:# That means the elevator has to go down
              self.y += time_past * MOVE_ELEVATOR

          elif self.y - time_past * MOVE_ELEVATOR > self.location.y:#That means the elevator has to go up
              self.y -= time_past * MOVE_ELEVATOR

          else: # That means the elevator has arrived
              self.location.floor_button.exchange_color_to_grae_and_Sound_ding ()
              self.location.Occupy_the_floor()
              if self.location.time.time <= -2:     
                if self.Q:
                    self.location.Release_the_floor()
                    self.location = self.Q.pop (0)


    def plot_Elevator(self,screen):
        screen.blit((self.img_Elevator),(self.x,self.y))
