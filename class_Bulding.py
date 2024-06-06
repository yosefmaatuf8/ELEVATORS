import pygame as pg
import time
from setting import *
from class_Floor import*
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
            
    
    
