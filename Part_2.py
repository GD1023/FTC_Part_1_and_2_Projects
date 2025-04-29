import pygame
import sys
import random

BLACK = (0, 0, 0)
BLUE= (0,0,255)
YELLOW= (255,255,0)


# Create the starting screen
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Falling Sand")
grid=[]
# Here I am creating a grid with 800 rows and 800 columns

for a in range(80):
    row = []
    for b in range(80):
        row.append(0)
    grid.append(row)

def draw_square(x,y,val):
    if val == 1: # Water box being created
        rectangle = pygame.Rect(x * 10, y * 10, 10, 10)
        pygame.draw.rect(screen, BLUE, rectangle)
    elif val==2: # Sand box being created
        rectangle = pygame.Rect(x * 10, y * 10, 10, 10)
        pygame.draw.rect(screen, YELLOW, rectangle)
    else:
        rectangle = pygame.Rect(x * 10, y * 10, 10, 10)
        pygame.draw.rect(screen, BLACK, rectangle)


def update_screen():

    for y in range(78,-1,-1):
        for x in range(79):
            if grid[y][x] == 2:  # Sand
                if grid[y + 1][x] == 0: #Sand falling down
                    grid[y][x], grid[y + 1][x] = 0, 2
                elif grid[y+1][x] == 1:
                    grid[y+1][x],grid[y][x] = 2,1
                elif x > 0 and grid[y + 1][x - 1] == 0:
                    grid[y][x], grid[y + 1][x - 1] = 0, 2
                elif x < 79 and grid[y + 1][x + 1] == 0:
                    grid[y][x], grid[y + 1][x + 1] = 0, 2
                else:
                    grid[y][x]=2

            if grid[y][x] == 1:  # Water
                if grid[y + 1][x] == 0:
                    grid[y][x], grid[y + 1][x] = 0, 1
                else:
                    if x > 0 and grid[y][x - 1] == 0:
                        grid[y][x], grid[y][x - 1] = 0, 1
                    elif x < 79 and grid[y][x + 1] == 0:
                        grid[y][x], grid[y][x + 1] = 0, 1


while True:
    # this is just a constant loop listening for user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.mouse.get_pressed()[0]:  # THis is for left click
            mousex, mousey = pygame.mouse.get_pos()
            grid[(mousey // 10)%80][(mousex // 10)%80] = 1

        if pygame.mouse.get_pressed()[2]:
            mousex, mousey = pygame.mouse.get_pos()
            grid[(mousey // 10)%80][(mousex // 10)%80] = 2

    for y in range(80):
        for x in range(80):
            draw_square(x, y, grid[y][x])
    update_screen()
    pygame.display.update()