from setting import *
import pygame as pg
import time
from estate import *

    
class Button:
    """
    Represents a button associated with a floor in a building.

    Attributes:
        color (int): The color of the button (0 for gray, 1 for green).
        number_floor (int): The number of the floor associated with the button.
        x (int): X-coordinate of the button.
        y (int): Y-coordinate of the button.
        button_erea (pygame.Rect): Rectangle representing the clickable area of the button.
    """
    

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
        """
        Changes the button color to gray and plays a sound When the elevator reaches the floor
        """
        if self.color == 1:
            self.color = 0
            pg.mixer.Sound.play(self.ding)


    def plot_Button(self,screen,font):
        img_i = self.arr[ self.color]
        screen.blit((img_i),(self.x,self.y))
        screen.blit(font.render(str(self.number_floor),True,(0,0,0)),(self.x + NUMBER_FLOOR_LOCATION[0],self.y + NUMBER_FLOOR_LOCATION[1]))
