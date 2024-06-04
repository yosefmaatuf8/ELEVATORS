WINDOW_X = 1000 # WINDOW_X > 500
WINDOW_Y = 800
DING = "/home/mefathim/Downloads/ding (mp3cut.net).mp3"
BOTTOM_SPACE = 100
LEFT_SPACE = 200
IMG_BRICK_WALL ='/home/mefathim/Downloads/AdobeStock_450024577_Preview.jpeg.png'
IMG_BRICK_WALL_SIZE = (150, 43) # (x, y)
IMG_ELEVATOR = '/home/mefathim/.cache/.fr-e3Yykj/ElevatorChallenge - Python/elv.png'
IMG_ELEVATOR_SIZE = (30, 30) 
TIMER_SIZE = (30 ,IMG_BRICK_WALL_SIZE[1] + 7) # the size of the timer near the floor
IMG_BOTTON_SIZE= (30,25)
IMG_LINE_SIZE=(150,7)
FLOOR_SIZE = (IMG_BRICK_WALL_SIZE[0] + TIMER_SIZE[0], IMG_BRICK_WALL_SIZE[1] + IMG_LINE_SIZE[1]) # by default: (50, 200)
ELEVATOR_SIZE = (IMG_ELEVATOR_SIZE[0]+7 ,FLOOR_SIZE[1]) # by default: (50, 50)
BUTTON_SIZE= (IMG_BOTTON_SIZE [0]+5,IMG_BOTTON_SIZE[1]+5)
FONT='/home/mefathim/Downloads/Rubik-Regular.ttf'
PLOT_TIME=1/60
FLOOR_NUMBER = 15
SPEED = 0.5
ELEVATOR_X= LEFT_SPACE+FLOOR_SIZE[0] +7
ELEVATOR_NUMBER = 3
MOVE_ELEVATOR = (FLOOR_SIZE[1]/SPEED) 
TIMER_LOCATION_Y = 10  # 
BUTTON_LOCATION = (65,12)
BUTTON_EREA = (30,15)
NUMBER_FLOOR_LOCATION = (9,5)


# def initialize_timer(x,y):




# height_floor=50
# FLOORS=10
# left_space=100
# height_space=700
# img_floor="/home/mefathim/Downloads/AdobeStock_450024577_Preview.jpeg.png"
# IMG_ELEVATOR="/home/mefathim/.cache/.fr-e3Yykj/ElevatorChallenge - Python/elv.png"

# def setting_corect():
#     if (WINDOW_Y -100)/FLOORS < height_floor:
#         # height= (y-100)/FLOORS
#         print("The parameters do not match the settings")
#         return False