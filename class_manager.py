import pygame as pg
import time
from setting import *
from elements import *
import math
from class_Building import *
from class_elevator import *
class manager:  
    """
      responsible for connection between the classes floor and elevatrs
    """
    def __init__(self) -> None:
        self.Building = Building()
        self.elevators = Elevator_system(self.Building.Floors[0])
        self.last_time = time.time()
        self.current_time=0
        self.time_past = 0
        self.background = pg.transform.scale (pg.image.load(IMG_SKY_BACKGROUND),(WORLD_SIZE[0],WORLD_SIZE[1]))

    def timer (self):
        """
        Updates the timer for the simulation.
        """
        self.current_time=time.time()
        time_past = self.current_time - self.last_time
        self.last_time = time.time()
        self.time_past = time_past
            
    def user_get_click(self,event: pg.event,scroll_x, scroll_y):
        """
        Handles user click events.

     Args:
        event (pg.event): The Pygame event object.
        scroll_x (int): The current scroll offset on the x-axis.
        scroll_y (int): The current scroll offset on the y-axis.
     """
        if event.type == pg.MOUSEBUTTONDOWN:
            event_pos = (event.pos[0] + scroll_x, event.pos[1] + scroll_y) 

            for floor_loop in self.Building.Floors:
                if floor_loop.get_Invitation_Button(event_pos,scroll_x, scroll_y):
                    elevator_near= self.elevators.chose_elevator(floor_loop)
                    floor_loop.update_values(elevator_near)


    def plot_manager(self,screen,font):
        self.timer()
        screen.blit(self.background,(0,0))
        self.Building.plot_Building(screen,font,self.time_past)
        self.elevators.plot_all_elevators(screen,self.time_past)
    
               


