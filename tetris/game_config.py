# 20 * 10 square grid, each grid will have 30 pixels
# When a block comes out, 
# if any block is already on it -> fail
# if right below has the block -> fails
import pygame
import numpy as np
import random
import time
grid_width = 35
grid_height = 35
grid_num_x = 10
grid_num_y = 20
VEL = 35
FPS = 15
WIDTH = grid_width * (grid_num_x)
HEIGHT = grid_height * (grid_num_y)


# Color
WHITE = (255,255,255)

# what do i need to define?

class shape:

    def __init__(self,type,index,status):
        self.main = type  # block type
        self.index = index
        self.status = status
        
    def get_coor(self):
        coor = np.zeros((4,2))
        i = 0
        j = 0
        for unit in self.main:
            coor[i][j] = unit.x
            coor[i][j+1] = unit.y
            i += 1
        return coor

    # if any block is already on it -> fail
    # if right below has the block -> fails
    def start_check(self):
        # if the block cannot move and any one of the block is touching the ceiling
        # 1) it can pop up and there is no room to move
        # 2) more extreme, it cannot actually be generated on tetris
        result = False
        for unit in self.main:
            if (unit.y // grid_height != 19) and self.status[unit.y  // grid_height][unit.x // grid_width] == 1:
                for unit in self.main:
                    if unit.y // grid_height == 0:
                        print("yessir")
                        print(self.get_coor())
                        return True
        return result

    def check_move(self):
        result = False
        for unit in self.main:
            if self.status[unit.y  // grid_height + 1][unit.x // grid_width] == 1: # if every block can move down
                result = True      
        return result

    def stack(self,shape_list):
        for unit in self.main:
            self.status[unit.y // grid_height][unit.x // grid_width] = 1
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
        shape_list.append(shape(random.choice(BLOCKS),len(shape_list),self.status))
        print(shape_list[-1].main)

    def handle_movement(self,shape_list,keys_pressed):
 
        if keys_pressed[pygame.K_DOWN]:
            for unit in self.main:
                unit.y += grid_height
            print(self.get_coor()[:,1] // grid_height)
            if 19 * grid_height in self.get_coor()[:,1]: # if one of the unit is on the ground
                self.stack(shape_list)
                self.start_check()
               # I see that the previous block gets pushed
            elif self.check_move(): # if one of the unit is on top of existing unit, stack
                self.stack(shape_list)
                self.start_check()

        











