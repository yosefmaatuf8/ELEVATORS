WINDOW_X = 1000 # WINDOW_X > 500
WINDOW_Y = 1000
FLOOR_NUMBER = 20
ELEVATOR_NUMBER = 5

DING = "ding_cut.mp3"
BOTTOM_SPACE = 50
LEFT_SPACE = 200
IMG_BRICK_WALL ='brick_wall.png'
IMG_LINE = 'line.png'
IMG_SKY_BACKGROUND='Sky background2.jpg'
IMG_BOTTON_GREEN = 'green_button.png'
IMG_BOTTON_GRAEY = 'grey_button.png'
IMG_BRICK_WALL_SIZE = (150, 43) # (x, y)
if (WINDOW_Y - BOTTOM_SPACE)/FLOOR_NUMBER < 50:
    IMG_BRICK_WALL_SIZE = (150,(WINDOW_Y - BOTTOM_SPACE)//FLOOR_NUMBER-7)
IMG_ELEVATOR = 'elv.png'
IMG_ELEVATOR_SIZE = (IMG_BRICK_WALL_SIZE[1]//1.2,IMG_BRICK_WALL_SIZE[1]//1.2) 
TIMER_SIZE = (30 ,IMG_BRICK_WALL_SIZE[1] + 7) # the size of the timer near the floor
IMG_LINE_SIZE=(150,7)
FLOOR_SIZE = (IMG_BRICK_WALL_SIZE[0] + TIMER_SIZE[0], IMG_BRICK_WALL_SIZE[1] + IMG_LINE_SIZE[1]) # by default: (50, 200)
ELEVATOR_SIZE = (IMG_ELEVATOR_SIZE[0]+7 ,FLOOR_SIZE[1]) # by default: (50, 50)
IMG_BOTTON_SIZE= (IMG_BRICK_WALL_SIZE[0]/5,FLOOR_SIZE[1]/2)
BUTTON_SIZE= (IMG_BOTTON_SIZE [0],IMG_BOTTON_SIZE[1])
FONT='Font.ttf'
SPEED = 0.5
ELEVATOR_X= LEFT_SPACE+FLOOR_SIZE[0]
MOVE_ELEVATOR = (FLOOR_SIZE[1]/SPEED) 
TIMER_LOCATION_Y = FLOOR_SIZE [1]/5 # 
BUTTON_LOCATION =  ((IMG_BRICK_WALL_SIZE[0]-BUTTON_SIZE[0])/2,(FLOOR_SIZE[1] - BUTTON_SIZE[1])/2)
BUTTON_EREA = (40,FLOOR_SIZE[1]/3)
NUMBER_FLOOR_LOCATION = (BUTTON_SIZE[0]//3,BUTTON_SIZE[1]/5)






def distance (floor_number_1:int,floor_number_2:int):
    distance=floor_number_1 - floor_number_2
    distance = distance if  distance > 0 else distance * -1 
    distance=Convert_distance_to_time(distance)
    return distance


def Convert_distance_to_time(distance):
    return (distance /FLOOR_SIZE [1] )* SPEED
