import pygame



# first the scree size
# the board is 6 * 7 board (but make it to 7*7 so that we can show)
WIDTH, HEIGHT = 800,850
white = (255,255,255)

grid_img = pygame.image.load('asset/image/board.jpg')
grid_img =  pygame.transform.scale(grid_img, (600,700))
red_img = pygame.image.load('asset/image/red.png')
red_img =  pygame.transform.scale(red_img, (100,100))

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Second Game, 4inarow")

def draw():
    WIN.fill(white)
    WIN.blit(grid_img, (100,100))
    WIN.blit(red_img, (100,100))

    pygame.display.update()

# game loop, infinite loop we will terminate when we 
# end the game
def main():
    pygame.init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()

        
    pygame.quit()

if __name__ == "__main__":
    main()