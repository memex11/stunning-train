#this code is adapted from invent with python book

import pygame, sys
from pygame.locals import *

pygame.init()

suspectlist = ['Eloy.png','Gray.png','Binod.png','Kraus.png']


FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

def clockwise(input_x,input_y,input_direction):

    if input_direction == 'right':
            input_x += 5
            if input_x ==400:
                input_direction = 'down'
    elif input_direction == 'down':
        input_y += 5
        if input_y ==600:
            input_direction = 'left'
    elif input_direction == 'left':
        input_x -= 5
        if input_x == 10:
            input_direction = 'up'
    elif input_direction == 'up':
        input_y -= 5
        if input_y ==10:
            input_direction = 'right'

    new_x = input_x
    new_y = input_y
    new_direction = input_direction

    # perhaps new and input are reserve words
    

    return new_x,new_y,new_direction

def counterwise(input_x,input_y,input_direction):

    if input_direction == 'right':
            input_x += 5
            if input_x ==400:
                input_direction = 'up'
    elif input_direction == 'down':
        input_y += 5
        if input_y ==600:
            input_direction = 'right'
    elif input_direction == 'left':
        input_x -= 5
        if input_x == 10:
            input_direction = 'down'
    elif input_direction == 'up':
        input_y -= 5
        if input_y ==10:
            input_direction = 'left'

    new_x = input_x
    new_y = input_y
    new_direction = input_direction

    # perhaps new and input are reserve words
    

    return new_x,new_y,new_direction

class Decisio_Picture_Deal:
    def __init__(self,x_part=100,y_part=100,direction_part='right',image_part='Eloy.png'):
        self.x = x_part
        self.y = y_part
        self.direction = direction_part
        self.Img = pygame.image.load(image_part)
        self.name = image_part.split('.')[0] #this splits the image name and makes a string

class Writing_Place:
    def __init__(self,person='Eloy',x_coord=100,y_coord=200):
        self.SurfaceObj = fontObj.render('{2} X:{0} Y:{1}'.format(person.x,person.y,person.name),True,GREEN,BLUE)
        self.RectObj = self.SurfaceObj.get_rect()
        self.RectObj.center = (x_coord,y_coord) # i see where these should refer to each other perhaps

def update_box_output(person):
    #print(person.name,person.x,person.y)
    person.SurfaceObj = fontObj.render('{2} X:{0} Y:{1}'.format(person.x,person.y,person.name),True,GREEN,BLUE)
    return person.SurfaceObj #return whole object or just a part

#window set up
DISPLAYSURF = pygame.display.set_mode((600,800))
pygame.display.set_caption('fontsnstuff')

#set up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)

#creates people objects
eloy = Decisio_Picture_Deal(10,10,'right','Eloy.png')
gray = Decisio_Picture_Deal(400,10,'left','Gray.png')
kraus = Decisio_Picture_Deal(100,50,'left','Kraus.png')


#text type declaration
fontObj = pygame.font.Font('freesansbold.ttf',32)

#this creates the text boxes

box_eloy =Writing_Place(eloy,200,300)
box_gray =Writing_Place(gray,200,250)
box_kraus=Writing_Place(gray,200,200)



while True: #main game loop
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(box_eloy.SurfaceObj,box_eloy.RectObj)
    DISPLAYSURF.blit(box_gray.SurfaceObj,box_gray.RectObj)

    DISPLAYSURF.blit(box_kraus.SurfaceObj,box_kraus.RectObj)
      
    eloy.x,eloy.y,eloy.direction = clockwise(eloy.x,eloy.y,eloy.direction )
    gray.x,gray.y,gray.direction = counterwise(gray.x,gray.y,gray.direction )
    
    kraus.x,kraus.y,kraus.direction = counterwise(kraus.x,kraus.y,kraus.direction )

    DISPLAYSURF.blit(eloy.Img,(eloy.x,eloy.y))
    DISPLAYSURF.blit(gray.Img,(gray.x,gray.y))

    DISPLAYSURF.blit(kraus.Img,(kraus.x,kraus.y))
    
    box_eloy.SurfaceObj = update_box_output(eloy)
    box_gray.SurfaceObj = update_box_output(gray)

    box_kraus.SurfaceObj = update_box_output(kraus)

     
    DISPLAYSURF.blit(box_eloy.SurfaceObj,box_eloy.RectObj)
    DISPLAYSURF.blit(box_gray.SurfaceObj,box_gray.RectObj)

    DISPLAYSURF.blit(box_kraus.SurfaceObj,box_kraus.RectObj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    

            

            

