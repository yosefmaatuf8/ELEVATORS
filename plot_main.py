import pygame as pg
from setting import *
from class_Bulding import *
def main_plot(Manager:object):

    pg.init()
    pg.font.init()
    font = pg.font.Font(FONT, IMG_BRICK_WALL_SIZE[1] // 3)

    screen = pg.display.set_mode((1000, 800))
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