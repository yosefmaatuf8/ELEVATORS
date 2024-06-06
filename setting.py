WINDOW_X = 1000 # WINDOW_X > 500
WINDOW_Y = 1000
FLOOR_NUMBER = 10
ELEVATOR_NUMBER = 10


DING = "/home/mefathim/python/ELEVATOR/ding_cut.mp3"
BOTTOM_SPACE = 100
LEFT_SPACE = 200
IMG_BRICK_WALL ='/home/mefathim/python/ELEVATOR/brick_wall.png'
IMG_LINE = '/home/mefathim/python/ELEVATOR/line.png'
IMG_SKY_BACKGROUND='/home/mefathim/python/ELEVATOR/Sky background.jpeg'
IMG_BRICK_WALL_SIZE = (150, 43) # (x, y)
IMG_ELEVATOR = '/home/mefathim/python/ELEVATOR/elv.png'
IMG_ELEVATOR_SIZE = (30,IMG_BRICK_WALL_SIZE[1]//1.4) 
TIMER_SIZE = (30 ,IMG_BRICK_WALL_SIZE[1] + 7) # the size of the timer near the floor
IMG_BOTTON_SIZE= (30,25)
IMG_LINE_SIZE=(150,7)
FLOOR_SIZE = (IMG_BRICK_WALL_SIZE[0] + TIMER_SIZE[0], IMG_BRICK_WALL_SIZE[1] + IMG_LINE_SIZE[1]) # by default: (50, 200)
ELEVATOR_SIZE = (IMG_ELEVATOR_SIZE[0]+7 ,FLOOR_SIZE[1]) # by default: (50, 50)
BUTTON_SIZE= (IMG_BOTTON_SIZE [0],IMG_BOTTON_SIZE[1])
FONT='/home/mefathim/Downloads/Rubik-Regular.ttf'
SPEED = 0.5
ELEVATOR_X= LEFT_SPACE+FLOOR_SIZE[0]
MOVE_ELEVATOR = (FLOOR_SIZE[1]/SPEED) 
TIMER_LOCATION_Y = FLOOR_SIZE [1]/5 # 
BUTTON_LOCATION =  ((IMG_BRICK_WALL_SIZE[0]-BUTTON_SIZE[0])/2,(FLOOR_SIZE[1] - BUTTON_SIZE[1])/2)
BUTTON_EREA = (40,15)
NUMBER_FLOOR_LOCATION = (9,5)



def setting_corect():
    if (WINDOW_Y - BOTTOM_SPACE)/FLOOR_NUMBER < FLOOR_SIZE[1]:

        print("The parameters do not match the settings")
        return False
    return True

def distance (floor_number_1:int,floor_number_2:int):
    distance=floor_number_1 - floor_number_2
    distance = distance if  distance > 0 else distance * -1 
    distance=Convert_distance_to_time(distance)
    return distance


def Convert_distance_to_time(distance):
    return (distance /FLOOR_SIZE [1] )* SPEED
