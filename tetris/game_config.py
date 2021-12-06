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


# Color
WHITE = (255,255,255)

# what do i need to define?

class shape:

    def __init__(self,type,index,status,last = 0):
        self.main = type  # block type
        self.index = index
        self.status = status
        self.stage = 0
        self.last = last
        if type == i:
            self.kind = "i"
        elif type == j:
            self.kind = "j"
        elif type == l:
            self.kind = "l"
        elif type == o:
            self.kind = "o"
        elif type == s:
            self.kind = "s"
        elif type == t:
            self.kind = "t"
        elif type == z:
            self.kind = "z"    

    def get_coor(self):
        coor = np.zeros((4,2))
        i = 0
        j = 0
        for unit in self.main:
            coor[i][j] = unit.x
            coor[i][j+1] = unit.y
            i += 1
        return coor
    
    def remove(self,unit):
        self.main.remove(unit)


    # if any block is already on it -> fail
    # if right below has the block -> fails
    def start_check(self):
        # if the block cannot move and any one of the block is touching the ceiling
        # 1) it can pop up and there is no room to move
        # 2) more extreme, it cannot actually be generated on tetris
        result = False
        for unit in self.main:
            if (unit.y // grid_height != 19):# and self.status[unit.y  // grid_height][unit.x // grid_width] == 1:
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

    def stack(self,shape_list,status,token):
        run = True
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
        multiple = len(shape_list) // 7
        orders = len(shape_list) % 7
        for order in range(orders):
            if shape_list[multiple * 7 + order].kind == "i":
                BLOCKS.remove(i)
            elif shape_list[multiple * 7 + order].kind == "j":
                BLOCKS.remove(j)  
            elif shape_list[multiple * 7 + order].kind == "l":
                BLOCKS.remove(l)   
            elif shape_list[multiple * 7 + order].kind == "o":
                BLOCKS.remove(o)   
            elif shape_list[multiple * 7 + order].kind == "s":
                BLOCKS.remove(s)   
            elif shape_list[multiple * 7 + order].kind == "t":
                BLOCKS.remove(t)   
            elif shape_list[multiple * 7 + order].kind == "z":
                BLOCKS.remove(z)                 
        temp = random.choice(BLOCKS)
        for unit in temp:
            if status[unit.y // grid_height][unit.x // grid_width] == 1 or status[unit.y // grid_height + 1][unit.x // grid_width] == 1 :
                print("returned False")
                if shape_list[-1].last == 0:
                    shape_list.append(shape(temp,len(shape_list),self.status,-1))
                return False
        if run:
            shape_list.append(shape(temp,len(shape_list),self.status))
        

    def handle_movement(self,keys_pressed,status,seconds, down = 1):
        que = True
        if keys_pressed[pygame.K_DOWN] or down ==0:
            for unit in self.main:
                unit.y += grid_height
        if keys_pressed[pygame.K_LEFT] and (self.get_coor()[:,0]>0).all():
            for unit in self.main:
                if status[unit.y // grid_height][unit.x // grid_height -1] == 1:
                    que = False
            if que:
                for unit in self.main:
                    unit.x -= grid_height
        if keys_pressed[pygame.K_RIGHT] and (self.get_coor()[:,0]<WIDTH-grid_width).all():
            for unit in self.main:
                if status[unit.y // grid_height][unit.x // grid_height + 1] == 1:
                    que = False
            if que:
                for unit in self.main:
                    unit.x += grid_height

        if keys_pressed[pygame.K_z] and time.time() - seconds > 0.2:
            seconds = time.time()
            x0 = self.main[0].x
            x1 = self.main[1].x
            x2 = self.main[2].x
            x3 = self.main[3].x
            y0 = self.main[0].y
            y1 = self.main[1].y
            y2 = self.main[2].y
            y3 = self.main[3].y
            stage = self.stage

            if self.kind == "i" and self.stage % 2 == 0:
                # if x >0 and x<20 and y > 0 and y <20
                self.main[0].x = self.main[0].x - grid_height
                self.main[0].y = self.main[0].y + grid_height
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y - grid_height
                self.main[3].x = self.main[3].x + 2*grid_height
                self.main[3].y = self.main[3].y - 2*grid_height
                self.stage = self.stage + 1

            elif self.kind == "i" and self.stage % 2 == 1:
                self.main[0].x = self.main[0].x + grid_height
                self.main[0].y = self.main[0].y - grid_height
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y + grid_height
                self.main[3].x = self.main[3].x - 2*grid_height
                self.main[3].y = self.main[3].y + 2*grid_height
                self.stage = self.stage + 1
            elif self.kind == "j" and self.stage % 4 == 0:
                self.main[0].x = self.main[0].x + 2*grid_height
                self.main[0].y = self.main[0].y - grid_height
                self.main[1].x = self.main[1].x + grid_height
                self.main[1].y = self.main[1].y - 2*grid_height
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y - grid_height                
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y 
                self.stage = self.stage + 1
            elif self.kind == "j" and self.stage % 4 == 1:
                self.main[0].x = self.main[0].x 
                self.main[0].y = self.main[0].y + 2*grid_height
                self.main[1].x = self.main[1].x + grid_height
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y                
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y - grid_height
                self.stage = self.stage + 1
            elif self.kind == "j" and self.stage % 4 == 2:
                self.main[0].x = self.main[0].x - 2 * grid_height
                self.main[0].y = self.main[0].y 
                self.main[1].x = self.main[1].x - grid_height
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y                
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y - grid_height
                self.stage = self.stage + 1
            elif self.kind == "j" and self.stage % 4 == 3:
                self.main[0].x = self.main[0].x 
                self.main[0].y = self.main[0].y - grid_height
                self.main[1].x = self.main[1].x - grid_height
                self.main[1].y = self.main[1].y 
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y  + grid_height          
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y + 2* grid_height
                self.stage = self.stage + 1 
            elif self.kind == "l" and self.stage % 4 == 0:
                self.main[0].x = self.main[0].x  + grid_height
                self.main[0].y = self.main[0].y - 2* grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y - grid_height
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y            
                self.main[3].x = self.main[3].x 
                self.main[3].y = self.main[3].y + grid_height
                self.stage = self.stage + 1  
            elif self.kind == "l" and self.stage % 4 == 1:
                self.main[0].x = self.main[0].x  + grid_height
                self.main[0].y = self.main[0].y + grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y 
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y - grid_height         
                self.main[3].x = self.main[3].x - 2* grid_height
                self.main[3].y = self.main[3].y 
                self.stage = self.stage + 1  
            elif self.kind == "l" and self.stage % 4 == 2:
                self.main[0].x = self.main[0].x - grid_height
                self.main[0].y = self.main[0].y + grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y 
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y - grid_height         
                self.main[3].x = self.main[3].x 
                self.main[3].y = self.main[3].y - 2* grid_height
                self.stage = self.stage + 1
            elif self.kind == "l" and self.stage % 4 == 3:
                self.main[0].x = self.main[0].x - grid_height
                self.main[0].y = self.main[0].y 
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y + 2*grid_height        
                self.main[3].x = self.main[3].x + 2*grid_height
                self.main[3].y = self.main[3].y + grid_height
                self.stage = self.stage + 1  
            elif self.kind == "s" and self.stage % 2 == 0:
                self.main[0].x = self.main[0].x 
                self.main[0].y = self.main[0].y - 2* grid_height
                self.main[1].x = self.main[1].x - grid_height
                self.main[1].y = self.main[1].y - grid_height
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y        
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y + grid_height
                self.stage = self.stage + 1                 
            elif self.kind == "s" and self.stage % 2 == 1:
                self.main[0].x = self.main[0].x 
                self.main[0].y = self.main[0].y + 2* grid_height
                self.main[1].x = self.main[1].x + grid_height
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x 
                self.main[2].y = self.main[2].y        
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y - grid_height
                self.stage = self.stage + 1  
            elif self.kind == "z" and self.stage % 2 == 0:
                self.main[0].x = self.main[0].x + 2*grid_height
                self.main[0].y = self.main[0].y -  grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y - grid_height
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y        
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y
                self.stage = self.stage + 1 
            elif self.kind == "z" and self.stage % 2 == 1:
                self.main[0].x = self.main[0].x - 2*grid_height
                self.main[0].y = self.main[0].y +  grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y        
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y
                self.stage = self.stage + 1                         
            elif self.kind == "t" and self.stage % 4 == 0:
                self.main[0].x = self.main[0].x  + grid_height
                self.main[0].y = self.main[0].y - 2*  grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y - grid_height
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y        
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y
                self.stage = self.stage + 1                 
            elif self.kind == "t" and self.stage % 4 == 1:
                self.main[0].x = self.main[0].x  + grid_height
                self.main[0].y = self.main[0].y  +  grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y 
                self.main[2].x = self.main[2].x - grid_height
                self.main[2].y = self.main[2].y - grid_height       
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y +  grid_height
                self.stage = self.stage + 1                            
            elif self.kind == "t" and self.stage % 4 == 2:
                self.main[0].x = self.main[0].x  - grid_height
                self.main[0].y = self.main[0].y  +  grid_height
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y 
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y - grid_height       
                self.main[3].x = self.main[3].x - grid_height
                self.main[3].y = self.main[3].y -  grid_height
                self.stage = self.stage + 1

            elif self.kind == "t" and self.stage % 4 == 3:
                self.main[0].x = self.main[0].x  - grid_height
                self.main[0].y = self.main[0].y  
                self.main[1].x = self.main[1].x 
                self.main[1].y = self.main[1].y + grid_height
                self.main[2].x = self.main[2].x + grid_height
                self.main[2].y = self.main[2].y + 2* grid_height       
                self.main[3].x = self.main[3].x + grid_height
                self.main[3].y = self.main[3].y 
                self.stage = self.stage + 1   
            for unit in self.main:
                if unit.x//grid_height <0 or unit.x//grid_height > 9 or unit.y//grid_height <0 or unit.y//grid_height >19:
                    self.main[0].x = x0
                    self.main[1].x = x1
                    self.main[2].x = x2
                    self.main[3].x = x3
                    self.main[0].y = y0
                    self.main[1].y = y1
                    self.main[2].y = y2
                    self.main[3].y = y3
                    self.stage = stage
            if stage != self.stage:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/sound/rotation.ogg'))
        return seconds
    def update(self,shape_list,status,token):
        if 19 * grid_height in self.get_coor()[:,1]: # if one of the unit is on the ground
            if self.stack(shape_list,status,token)== False:
                return False
            # I see that the previous block gets pushed
        elif self.check_move(): # if one of the unit is on top of existing unit, stack
            if self.stack(shape_list,status,token)== False:
                return False
        











