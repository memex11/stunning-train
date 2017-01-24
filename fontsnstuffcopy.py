#this code is adapted from invent with python book

import pygame, sys
from pygame.locals import *

pygame.init()

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


#window set up
DISPLAYSURF = pygame.display.set_mode((600,800))
pygame.display.set_caption('fontsnstuff')

#set up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)

eloyImg = pygame.image.load('/home/pi/Desktop/Eloy.png')
eloy_x = 10
eloy_y =10
eloy_direction = 'right'


grayImg = pygame.image.load('/home/pi/Desktop/Gray.png')
gray_x = 100
gray_y = 50
gray_direction = 'left'

fontObj = pygame.font.Font('freesansbold.ttf',32)

text_GraySurfaceObj = fontObj.render('Gray X:{0} Y:{1}'.format(gray_x,gray_y),True,GREEN,BLUE)
text_GrayRectObj = text_GraySurfaceObj.get_rect()
text_GrayRectObj.center =(200,300)

text_EloySurfaceObj = fontObj.render('Eloy X:{0} Y:{1}'.format(eloy_x,eloy_y),True,GREEN,BLUE)
text_EloyRectObj = text_EloySurfaceObj.get_rect()
text_EloyRectObj.center =(200,150)


while True: #main game loop
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(text_GraySurfaceObj,text_GrayRectObj)
    DISPLAYSURF.blit(text_EloySurfaceObj,text_EloyRectObj)
    
  # I see that some sort of class object might be the next step
  
    eloy_x,eloy_y,eloy_direction = clockwise(eloy_x,eloy_y,eloy_direction )
    gray_x,gray_y,gray_direction = counterwise(gray_x,gray_y,gray_direction )


    DISPLAYSURF.blit(eloyImg,(eloy_x,eloy_y))
    DISPLAYSURF.blit(grayImg,(gray_x,gray_y))
    
    text_EloySurfaceObj = fontObj.render('Eloy X:{0} Y:{1}'.format(eloy_x,eloy_y),True,GREEN,BLUE)
    text_GraySurfaceObj = fontObj.render('Gray X:{0} Y:{1}'.format(gray_x,gray_y),True,GREEN,BLUE)

    DISPLAYSURF.blit(text_GraySurfaceObj,text_GrayRectObj)
    DISPLAYSURF.blit(text_EloySurfaceObj,text_EloyRectObj)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    

            

            

