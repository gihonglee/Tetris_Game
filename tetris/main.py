from numpy.core.defchararray import index
import game_config as g
from game_config import shape
import pygame
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



WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")
block_img = pygame.image.load('IMG_1598.png')
block_img =  pygame.transform.scale(block_img, (g.grid_width,g.grid_height))

def draw2(shape_list):
    WIN.fill(g.WHITE)
    for shape in shape_list:
        for unit in shape.main:
            WIN.blit(block_img, (unit.x, unit.y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    status = np.zeros((g.grid_num_y,g.grid_num_x))
    shape = g.shape(random.choice(BLOCKS),0,status)
    shape_list = [shape]
    run = True
    j = 0
    while run:
        j += 1
        clock.tick(g.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        shape_list[-1].handle_movement(shape_list,keys_pressed)
        if shape_list[-1].start_check():
            run = False
            time.sleep(5)




        draw2(shape_list)

    pygame.quit()


if __name__ == "__main__":
    main()

