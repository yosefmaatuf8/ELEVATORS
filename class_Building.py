import pygame as pg
import time
from setting import *
from class_Floor import*
import math
from elements import *

class Building:
    def __init__(self):
        self.Floors=[]
        self.initialize_floors()

    def initialize_floors(self):
        x=LEFT_SPACE
        y=WORLD_SIZE[1]-BOTTOM_SPACE  
        for i in range(FLOOR_NUMBER):
           self. Floors.append(Floor(i,x,y))
           y -= FLOOR_SIZE[1]
    def plot_Building (self,screen,font,time_past):
        for floor_loop in self.Floors:
             floor_loop.plot_floor(screen,font,time_past)      
            
    
    
