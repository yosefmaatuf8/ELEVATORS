# WINDOW_X = 1000 # WINDOW_X > 500
# WINDOW_Y = 1000
# IMG_BRICK_WALL_SIZE = (150, 43) # (x, y)
# if (WINDOW_Y - BOTTOM_SPACE)/FLOOR_NUMBER < 50:
#     IMG_BRICK_WALL_SIZE = (150,(WINDOW_Y - BOTTOM_SPACE)//FLOOR_NUMBER-(WINDOW_Y - BOTTOM_SPACE)//FLOOR_NUMBER//6)

FLOOR_NUMBER = 40
ELEVATOR_NUMBER = 10


BOTTOM_SPACE = 50
LEFT_SPACE = 200


IMG_BRICK_WALL_SIZE = (150, 43) # (x, y)
IMG_ELEVATOR_SIZE = (IMG_BRICK_WALL_SIZE[1]//1.2,IMG_BRICK_WALL_SIZE[1]//1.2) 
TIMER_SIZE = (30 ,IMG_BRICK_WALL_SIZE[1] + 7) # the size of the timer near the floor
IMG_LINE_SIZE=(150, IMG_BRICK_WALL_SIZE[1]//6)
FLOOR_SIZE = (IMG_BRICK_WALL_SIZE[0] + TIMER_SIZE[0], IMG_BRICK_WALL_SIZE[1] + IMG_LINE_SIZE[1]) # by default: (50, 200)
ELEVATOR_SIZE = (IMG_ELEVATOR_SIZE[0]+7 ,FLOOR_SIZE[1]) # by default: (50, 50)
IMG_BOTTON_SIZE= (IMG_BRICK_WALL_SIZE[0]/5,FLOOR_SIZE[1]/2)
BUTTON_SIZE= (IMG_BOTTON_SIZE [0],IMG_BOTTON_SIZE[1])


ELEVATOR_X= LEFT_SPACE+FLOOR_SIZE[0] # The location of the first elevator
TIMER_LOCATION_Y = FLOOR_SIZE [1]/5 # The position of the timer in relation to the floor
BUTTON_LOCATION =  ((IMG_BRICK_WALL_SIZE[0]-BUTTON_SIZE[0])/2,(FLOOR_SIZE[1] - BUTTON_SIZE[1])/2) # The position of the button in relation to the floor
BUTTON_EREA = (40,FLOOR_SIZE[1]/3) # Defining the area that will receive a click around the button location
NUMBER_FLOOR_LOCATION = (BUTTON_SIZE[0]//3,BUTTON_SIZE[1]/5)# The position of the digits representing the floor number in relation to the floor

# Define the size of the displayed screen and the size of the world
WORLD_SIZE = [(50 * 4) + FLOOR_SIZE[0] + (ELEVATOR_NUMBER * ELEVATOR_SIZE[0]), 100 +( FLOOR_NUMBER * FLOOR_SIZE[1])]
SCREEN_SIZE = (1200 if 1200 < WORLD_SIZE[0] else WORLD_SIZE[0], 1000 if 1000 < WORLD_SIZE[1] else WORLD_SIZE[1]) 
BACKGROUND = (100, 149, 237)


SPEED = 0.5
MOVE_ELEVATOR = (FLOOR_SIZE[1]/SPEED) 






def distance (floor_number_1:int,floor_number_2:int): 
    """
    Calculates the distance between two floorsin seconds.
    Returns:
        float: The distance between the two floors.
    """
    distance=floor_number_1 - floor_number_2
    distance = distance if  distance > 0 else distance * -1 
    return  (distance /FLOOR_SIZE [1] )* SPEED


