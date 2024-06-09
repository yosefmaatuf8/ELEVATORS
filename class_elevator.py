import pygame as pg
import time
from setting import *       
from elements import *

    
    
class Elevator_system:
    """
    Represents an elevator system managing multiple elevators.

    Attributes:
        Elevators (list): List of Elevator objects in the system.
    """
    def __init__(self,floor_0):
        self.Elevators=[]
        self.initialize_Elevators(floor_0)
        
        
    def initialize_Elevators(self,floor_0):
        x = LEFT_SPACE + FLOOR_SIZE[0]
        y = WORLD_SIZE[1]-BOTTOM_SPACE
        for Elevators_i in range(ELEVATOR_NUMBER):  
            self.Elevators.append(Elevator(floor_0,x,y))
            x += ELEVATOR_SIZE[0]


    def nearest_elevator (self,floor):
        """
        Finds the nearest elevator to a given floor.

        Args:
            floor (Floor): The target floor.

        Returns:
            tuple: The nearest elevator object and the time it will take to reach the floor.
        """
        nearest=(-1,float('inf'))
        for elevator_i in self.Elevators:
            if elevator_i.Q:
                 time_i= elevator_i.Q [-1].time.get_time() + distance(floor.y,elevator_i.Q[-1].y)
            else:
                time_i = elevator_i.location.time.get_time() + distance (floor.y,elevator_i.location.y)      
            if nearest[1] > time_i:
                    nearest=(elevator_i,time_i) 
            
        return nearest
             

    def chose_elevator(self,floor): 
       elevator,time = self.nearest_elevator(floor)
       elevator.add_call_Elevator(floor)
       return time
    

    def plot_all_elevators(self,screen,time_past):
        for elevatot_i in self.Elevators:
            elevatot_i.update_x_y(time_past)
            elevatot_i.plot_Elevator(screen)



            
class Elevator:
    def __init__(self,floor_0,x,y) -> None:
        self.Q = []    
        self.location = floor_0
        self.x = x
        self.y= y
        self.img_Elevator= pg.transform.scale (pg.image.load(IMG_ELEVATOR),(IMG_ELEVATOR_SIZE))

    def add_call_Elevator(self,floor):
        self.Q.append(floor)


    def update_x_y(self,time_past):
          """Updates the x and y coordinates of the elevator towards its destination
            based on the elapsed time."""
          if self.y + time_past * MOVE_ELEVATOR < self.location.y:
              self.y += time_past * MOVE_ELEVATOR

          elif self.y - time_past * MOVE_ELEVATOR > self.location.y:
              self.y -= time_past * MOVE_ELEVATOR
          else: 
              self.location.floor_button.exchange_color_to_grae_and_Sound_ding ()
              self.location.occupied = True
              if self.location.time.time <= -2:     
                if self.Q:
                    self.location.occupied = False
                    self.location = self.Q.pop (0)


    def plot_Elevator(self,screen):

        screen.blit((self.img_Elevator),(self.x,self.y))
