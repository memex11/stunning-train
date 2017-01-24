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
    def __init__(self,x_part,y_part,direction_part,image_part):
        self.x = x_part
        self.y = y_part
        self.direction = direction_part
        self.Img = pygame.image.load(image_part)

        
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
gray = Decisio_Picture_Deal(100,50,'left','Gray.png')


fontObj = pygame.font.Font('freesansbold.ttf',32)

text_GraySurfaceObj = fontObj.render('Gray X:{0} Y:{1}'.format(gray.x,gray.y),True,GREEN,BLUE)
text_GrayRectObj = text_GraySurfaceObj.get_rect()
text_GrayRectObj.center =(200,300)

text_EloySurfaceObj = fontObj.render('Eloy X:{0} Y:{1}'.format(eloy.x,eloy.y),True,GREEN,BLUE)
text_EloyRectObj = text_EloySurfaceObj.get_rect()
text_EloyRectObj.center =(200,150)


while True: #main game loop
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(text_GraySurfaceObj,text_GrayRectObj)
    DISPLAYSURF.blit(text_EloySurfaceObj,text_EloyRectObj)
      
    eloy.x,eloy.y,eloy.direction = clockwise(eloy.x,eloy.y,eloy.direction )
    gray.x,gray.y,gray.direction = counterwise(gray.x,gray.y,gray.direction )


    DISPLAYSURF.blit(eloy.Img,(eloy.x,eloy.y))
    DISPLAYSURF.blit(gray.Img,(gray.x,gray.y))
    
    text_EloySurfaceObj = fontObj.render('Eloy X:{0} Y:{1}'.format(eloy.x,eloy.y),True,GREEN,BLUE)
    text_GraySurfaceObj = fontObj.render('Gray X:{0} Y:{1}'.format(gray.x,gray.y),True,GREEN,BLUE)

    DISPLAYSURF.blit(text_GraySurfaceObj,text_GrayRectObj)
    DISPLAYSURF.blit(text_EloySurfaceObj,text_EloyRectObj)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    

            

            

