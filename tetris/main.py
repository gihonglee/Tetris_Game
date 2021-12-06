from numpy.core.defchararray import index
import game_config as g
from game_config import shape
import pygame
from pygame.locals import *
from pygame import mixer
import numpy as np
import random
import time

grid_width = 35
grid_height = 35

i = [pygame.Rect(0,0, grid_width,grid_height),
pygame.Rect(0, grid_width,  grid_width, grid_height),
pygame.Rect(0, grid_width*2,  grid_width, grid_height),
pygame.Rect(0, grid_width*3,  grid_width, grid_height)]

j = [pygame.Rect(0,0, grid_width,grid_height),
pygame.Rect(0, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height)]

l = [pygame.Rect(0,grid_width, grid_width,grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width*2, 0,  grid_width, grid_height)]

o = [pygame.Rect(0,0, grid_width,grid_height),
pygame.Rect(0, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, 0,  grid_width, grid_height)]

s = [pygame.Rect(0,grid_width, grid_width,grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, 0,  grid_width, grid_height),
pygame.Rect(grid_width*2, 0,  grid_width, grid_height)]

t = [pygame.Rect(0,grid_width, grid_width,grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, 0,  grid_width, grid_height)]

z = [pygame.Rect(0,0, grid_width,grid_height),
pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
pygame.Rect(grid_width, 0,  grid_width, grid_height)]

BLOCKS = [i,j,l,o,s,t,z]

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
red = (255,0,0)

WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")
i_img = pygame.image.load('assets/image/i.png')
j_img = pygame.image.load('assets/image/j.png')
s_img = pygame.image.load('assets/image/s.png')
t_img = pygame.image.load('assets/image/t.png')
o_img = pygame.image.load('assets/image/o.png')
l_img = pygame.image.load('assets/image/l.png')
z_img = pygame.image.load('assets/image/z.png')
grid_img = pygame.image.load('assets/image/1.jpg')
i_img =  pygame.transform.scale(i_img, (g.grid_width,g.grid_height))
j_img =  pygame.transform.scale(j_img, (g.grid_width,g.grid_height))
s_img =  pygame.transform.scale(s_img, (g.grid_width,g.grid_height))
t_img =  pygame.transform.scale(t_img, (g.grid_width,g.grid_height))
o_img =  pygame.transform.scale(o_img, (g.grid_width,g.grid_height))
l_img =  pygame.transform.scale(l_img, (g.grid_width,g.grid_height))
z_img =  pygame.transform.scale(z_img, (g.grid_width,g.grid_height))
grid_img =  pygame.transform.scale(grid_img, (g.WIDTH,g.HEIGHT))
def draw2(shape_list,end,point):
    WIN.fill(white)
    WIN.blit(grid_img, (0,0))
      
    for shape in shape_list:
        if shape.kind == "i":
            for unit in shape.main:
                WIN.blit(i_img, (unit.x, unit.y))
        elif shape.kind == "j":
            for unit in shape.main:
                WIN.blit(j_img, (unit.x, unit.y))
        elif shape.kind == "s":
            for unit in shape.main:
                WIN.blit(s_img, (unit.x, unit.y))
        elif shape.kind == "t":
            for unit in shape.main:
                WIN.blit(t_img, (unit.x, unit.y))
        elif shape.kind == "o":
            for unit in shape.main:
                WIN.blit(o_img, (unit.x, unit.y))
        elif shape.kind == "l":
            for unit in shape.main:
                WIN.blit(l_img, (unit.x, unit.y))
        elif shape.kind == "z":
            for unit in shape.main:
                WIN.blit(z_img, (unit.x, unit.y))

    if end:
        font = pygame.font.Font('freesansbold.ttf', 32)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Game Over', True, red, black)
        score = font2.render('Final Point: ' + str(point), True, white, black)        
        textRect = text.get_rect()
        scoreRect = score.get_rect()
        textRect.center = (g.WIDTH // 2, g.HEIGHT // 2)
        scoreRect.center = (g.WIDTH // 2, g.HEIGHT // 2 + 32)
        WIN.blit(text, textRect)
        WIN.blit(score, scoreRect)

    pygame.display.update()

def check_complete(status):
    row_2b_deleted = []
    sum_row = status.sum(axis=1)
    for i,row in enumerate(sum_row):
        if row == g.grid_num_x:
            row_2b_deleted.append(i)
    return row_2b_deleted
    # now we know the row, we know the height. we can simply visit blocks and delete them + status -> 0
    # all other units above has to descend by the number of floors that has been deleted
def delete_units(status,shape_list,j,point):
    complete_rows = check_complete(status)
    delete = False
    i = 0
    if len(complete_rows) >0:
        while i < 10 * len(complete_rows):
            for block in shape_list:
                for unit in block.main:
                    if unit.y // g.grid_height != 0 and unit.y // g.grid_height in complete_rows:
                        block.remove(unit)
                        i = i + 1
                        delete = True
    
    if delete:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sound/tetris.ogg'))  
        point = point + len(complete_rows)*10
        for i in complete_rows:
            for j in range(g.grid_num_x):
                status[i][j] = 0
        for block in shape_list:
            for unit in block.main:
                descend = 0
                for complete in complete_rows:
                    if unit.y // g.grid_height < complete and status[unit.y // g.grid_height][unit.x // g.grid_height] == 1:
                        descend += 1
                if descend >0:
                    unit.y = unit.y + descend * g.grid_height
        for i in range(g.grid_num_y):
            for j in range(g.grid_num_x):
                status[i][j] = 0
        for block in shape_list[0:len(shape_list)-1]:
            for unit in block.main:
                status[unit.y //g.grid_height][unit.x//g.grid_width] = 1
    return point




# i am confused because when I delete units and then update the status there should be no relationship btw
def delete_row(status):
    z = check_complete(status)
    for j in z:
        for i in range(g.grid_num_x): 
            status[j][i] = 0

def main():
    pygame.init()
    clock = pygame.time.Clock()
    status = np.zeros((g.grid_num_y,g.grid_num_x))
    shape = g.shape(random.choice(BLOCKS),0,status)
    shape_list = [shape]
    run = True
    end = False
    point = 0
    j = 0
    token = 0
    seconds = time.time()
    mixer.init()
    # mixer.music.load('bgm.ogg')
    # mixer.music.play()

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sound/bgm.ogg'))
    
    while run:
        clock.tick(g.FPS)
        j += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if j % g.FPS == 0:
            seconds = shape_list[-1].handle_movement(keys_pressed,status,seconds,0)
            shape_list[-1].update(shape_list,status,token)
            point = delete_units(status,shape_list,j,point)
            draw2(shape_list,end,point)
                     
        keys_pressed = pygame.key.get_pressed()
        seconds = shape_list[-1].handle_movement(keys_pressed,status, seconds)
        if shape_list[-1].update(shape_list,status,token) == False:
           end = True
        point = delete_units(status,shape_list,j,point)
        draw2(shape_list,end,point)
      
        if end:
            run = False
            time.sleep(3)
    pygame.quit()


if __name__ == "__main__":
    main()

