import pygame
import sys

# constants to remember

# So the screen size is 800 by 800,
# With 800 rows and columns
ROWS, COLS = 800,800
CELL_SIZE=5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the starting screen
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Conway's Game of Life")


grid=[]
# Here I am creating a grid with 800 rows and 800 columns
for a in range(ROWS):
    row = []
    for b in range(COLS):
        row.append(0)
    grid.append(row)

running = False
# Everytime the simulation completes the conditions, the screen is updated accordingly using this function( Just turning the squared either black or white)
def update_screen():
    screen.fill(BLACK)
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] == 1:
                rectangle = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rectangle)


def neighbors_sum(grid, row, col):
    neighbors=0
    for horizontal_shift in range (-1,2):
        for vertical_shift in range(-1,2):
            if horizontal_shift == 0 and vertical_shift == 0:
                continue
            else:
                r_cor= (row+vertical_shift)
                c_cor= (col+horizontal_shift)
            if 0 <= r_cor < ROWS and 0 <= c_cor < COLS:
                neighbors += grid[r_cor][c_cor]
    return neighbors

while True:
    # this is just a constant loop listening for user inputs
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.mouse.get_pressed()[0]: # THis is for left click
            mousex, mousey= pygame.mouse.get_pos()
            grid[mousey//CELL_SIZE][mousex//CELL_SIZE]=1

        if pygame.mouse.get_pressed()[2]:
            mousex,mousey= pygame.mouse.get_pos()
            grid[mousey // CELL_SIZE][mousex//CELL_SIZE]=0
            rectangle_1 = pygame.Rect(mousex*CELL_SIZE, mousey*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rectangle_1)

        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running    # The reason why we use not running, rather than just flipping running to True has to do with the fact that if we click the space bar again, the code should stop, thus running shoul;d be the opposite of what it was originally.


   # once the user clicks the space bar to start the program,  this is initiated.
    if running:
        new_grid=[]
        for a in range(ROWS):
            row = []
            for b in range(COLS):
                row.append(0)
            new_grid.append(row)

        for r in range(ROWS):
            for c in range(COLS):
                # using the function we previously defined to evaluate whether the cell dies or stays alive
                neighbors= neighbors_sum(grid, r, c)
                if grid[r][c] ==1:
                    if neighbors<2 or neighbors>3:
                        new_grid[r][c]=0
                    else:
                        new_grid[r][c]=1
                else:
                    if neighbors==3:
                        new_grid[r][c]=1
        # Once the evaluation is complete, everything is updated onto the screen
        grid=new_grid
    update_screen()
    pygame.display.update()










