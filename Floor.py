    
from setting import *
import pygame as pg
import time
from Timer import *
from Button import*
from estate import *

class Floor:
    """
    Represents a floor in a building.

    Attributes:
        occupied (bool): Indicates if the floor is occupied.
        floor_button (Button): Button associated with the floor.
    """
    def __init__ (self,number_floor,x,y):
        self.number_floor = number_floor
        self.occupied = False
        self.img = pg.transform.scale (pg.image.load(IMG_BRICK_WALL),IMG_BRICK_WALL_SIZE)
        self.line = pg.transform.scale (pg.image.load(IMG_LINE),(IMG_LINE_SIZE))
        self.x = x
        self.y = y
        self.floor_button=Button(self.number_floor,self.x,self.y)
        self.time = Timer(self.number_floor,self.x,self.y)


    def get_Invitation_Button(self,event_pos,scroll_x, scroll_y):
        """
        Checks if the invitation button is clicked.
        Args:
            event_pos: Position of the mouse click.
        Returns:
            bool: True if the button is clicked and floor not occupied, False otherwise.
        """
        if self.floor_button.button_erea.collidepoint(event_pos):
            if not self.occupied:
              return True
        return False
    

    def Update_values_when_an_elevator_is_ordered(self,time):
        self.Occupy_the_floor()
        self.time.set_time (time)
        self.floor_button.color = 1
 

    def Release_the_floor(self):
        self.occupied = False


    def Occupy_the_floor(self):
        self.occupied = True


    def plot_floor(self,screen,font,time_past):
        screen.blit(self.img,(self.x,self.y))
        if self.number_floor < FLOOR_NUMBER - 1:
            screen.blit(self.line,(self.x,self.y-IMG_LINE_SIZE[1]))           
        self.floor_button.plot_Button(screen,font)
        self.time.update_time(time_past)
        self.time.plot_time(screen,font)
