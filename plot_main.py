import pygame as pg
from setting import *
from class_Building import *
# def main_plot(Manager:object):

# # Initializes Pygame, sets up the display, and runs the main event loop.

#     pg.init()
#     pg.font.init()
#     if FLOOR_NUMBER<30:
#         font = pg.font.Font(FONT, IMG_BRICK_WALL_SIZE[1] //3)
#     else:
#         font = pg.font.Font(FONT, IMG_BRICK_WALL_SIZE[1] //2)
#     screen = pg.display.set_mode((WINDOW_X, WINDOW_Y))
#     clock = pg.time.Clock()

#     # here initialize items
#     run=True

#     while run:
#         clock.tick(200)
#         screen.fill((255, 255, 255))



#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 run=False
#             # here update index of items if depends on input
#             if event.type==pg.MOUSEBUTTONDOWN:
#                Manager.user_get_click (event.pos)
#         # here plot everything
        
#         Manager.plot_manager(screen,font)
    

    
#         pg.display.update()
#     pg.quit()






def main_plot(Manager:object):


    pg.init()
    pg.font.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    # the font for char that on the screen
    font = pg.font.Font(FONT, FLOOR_SIZE[1] // 3)


    # here initialize items

    world = pg.Surface((WORLD_SIZE[0], WORLD_SIZE[1]))
    world.fill(BACKGROUND)


    # Variables to track the offset of the visible window within the larger world

    scroll_x, scroll_y = 0, WORLD_SIZE[1] - SCREEN_SIZE[1]
    scroll_speed = 20  # Pixels per key press
    run = True

    while run:
        clock.tick(60)
        world.fill(BACKGROUND)


        for event in pg.event.get():
            if event.type == pg.QUIT:
              run = False  
            Manager.user_get_click(event, scroll_x, scroll_y)
        
        keys = pg.key.get_pressed()

        # Update scroll position based on arrow key presses
        if keys[pg.K_LEFT]:
            scroll_x = max(scroll_x - scroll_speed, 0)
        if keys[pg.K_RIGHT]:
            scroll_x = min(scroll_x + scroll_speed, WORLD_SIZE[0] - SCREEN_SIZE[0])
        if keys[pg.K_UP]:
            scroll_y = max(scroll_y - scroll_speed, 0)
        if keys[pg.K_DOWN]:
            scroll_y = min(scroll_y + scroll_speed, WORLD_SIZE[1] - SCREEN_SIZE[1])
 
        
       
        Manager.plot_manager(world, font)  
        screen.blit(pg.transform.scale(world, WORLD_SIZE), (0, 0), (scroll_x, scroll_y, SCREEN_SIZE[0] , SCREEN_SIZE[1]))      


        pg.display.update()