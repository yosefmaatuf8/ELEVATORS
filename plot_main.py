import pygame as pg
from setting import *
from class_Bulding import *
def main_plot(Manager:object):

# Initializes Pygame, sets up the display, and runs the main event loop.

    pg.init()
    pg.font.init()
    if FLOOR_NUMBER<30:
        font = pg.font.Font(FONT, IMG_BRICK_WALL_SIZE[1] //3)
    else:
        font = pg.font.Font(FONT, IMG_BRICK_WALL_SIZE[1] //2)
    screen = pg.display.set_mode((WINDOW_X, WINDOW_Y))
    clock = pg.time.Clock()

    # here initialize items
    run=True

    while run:
        clock.tick(200)
        screen.fill((255, 255, 255))



        for event in pg.event.get():
            if event.type == pg.QUIT:
                run=False
            # here update index of items if depends on input
            if event.type==pg.MOUSEBUTTONDOWN:
               Manager.user_get_click (event.pos)
        # here plot everything
        
        Manager.plot_manager(screen,font)
    

    
        pg.display.update()
    pg.quit()
