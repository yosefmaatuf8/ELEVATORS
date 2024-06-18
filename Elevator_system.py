import pygame as pg
import time
from setting import *       
from estate import *
from Elevator import *
    
    
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
       """Select an elevator for a reservation on a certain floor"""
       elevator,time = self.nearest_elevator(floor)
       elevator.add_call_Elevator(floor)
       return time
    

    def plot_all_elevators(self,screen,time_past):
        for elevatot_i in self.Elevators:
            elevatot_i.move_elevator(time_past)
            elevatot_i.plot_Elevator(screen)
