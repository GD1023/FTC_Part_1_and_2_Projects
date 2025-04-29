## April 12th, 2025

Today, I spent time trying to understand the FTC project better.  
Specifically, I focused on grasping the concept behind Conway’s Game of Life and its rules. I watched a few YouTube videos to deepen my understanding of how the simulation works.  
Afterward, I started thinking about how to translate the simulation into Python code.

**Important Rules to Remember:**
- If a live cell has fewer than 2 neighbors → it dies (underpopulation).
- If a live cell has more than 3 neighbors → it dies (overpopulation).
- If a live cell has 2 or 3 neighbors → it survives.
- If a dead cell has exactly 3 neighbors → it becomes alive (reproduction).

---

## April 13th, 2025

Today, I continued exploring the best way to implement Part 1 of the project (cellular automata / Conway’s Game of Life).

**My current plan:**
- I will create an 80x80 grid, represented as a list of lists, where each cell initially has a value of 0 (dead), as required.
- When the user interacts with the grid (for example, clicking a cell to turn it alive or dead), I will calculate the exact cell by dividing the mouse click coordinates by the cell size.
- I will update the grid based on the user’s interactions.
- Once the user hits the spacebar to start the simulation, the program will process the rules:
  - It will check each cell according to the Game of Life conditions listed above.
  - There will actually be two grids:
    - The current grid (representing the current state).
    - The next grid (where the updated state is stored).
  - After each iteration, the next grid will replace the current grid.

---

## April 14th, 2025

Today, I spent time implementing the plan in code. Here's what I did:

- I created an 80x80 grid to represent the board (just for now to test my code).
- I wrote two main functions:
  - update_screen(): Updates the display after the user interacts with the grid.
  - neighbor_sum(row, col): Calculates the sum of alive neighbors for a given cell. Since cells are either 0 (dead) or 1 (alive), the sum directly tells me how many alive neighbors there are.

I had to take a pause due to the extensive number of tests I have lined up this week. I look forward to completing the rest over spring break :)

---

## April 19th, 2025

I set up a while True loop for continuous simulation. Inside the loop:

- I listen for user events (quitting the game, mouse clicks).
- For mouse clicks:
  - Left click: Turns the clicked cell alive (value = 1).
  - Right click: Turns the clicked cell dead (value = 0).
- When updating the cells:
  - Instead of iterating through all 640,000 cells every time (which would be inefficient), I optimize by focusing only on alive cells.

Black cells represent dead cells, and white cells represent alive cells.

---

## April 20th, 2025

I spent time understanding the project for the Falling Sand simulation and played around with the given website for inspiration (this project is honestly pretty cool!).

**The rules for sand are simple:**
- If there is an empty space below the cell, the sand should fall down.
- If the space below is already filled with sand, the sand should move left or right.
- If the sand cannot move in any direction, it should stay put.

**The rules I came up with for water:**
- If there is an empty space below the cell, the water should fall down.
- If the space below is already filled, check bottom left and right for possible moves.
- If that is not possible, the water should move towards the left and level out.

One issue I faced was that when the water cannot go left or right, I was not able to make it proportionally fall on both sides to level out the water block. I hope to work more on this.

---

## April 22nd, 2025

Today, I planned out how I'm going to go about the project. I'm using Python, specifically the Pygame library.

**Initial setup:**
- I created stationary values for the colors: black (empty space), blue (water), and yellow (sand).
- I created the starting screen and an 80x80 grid. The purpose of the grid is to help map the current location of pre-existing squares (water or sand).
- I then created a function called draw_square(x, y, val), which:
  - Takes in x and y values and val to identify whether the square is water, sand, or empty.
  - Allocates the dimensions and position to a variable called rectangle, and draws it using pygame.draw.

---

## April 24th, 2025

Today I created an update_screen() function that carries out the movement logic for sand and water blocks.

- I started from the bottom of the grid and moved upwards.  
- The reason is to ensure I map out all the pre-existing grid values before making the current block move accordingly.

---

## April 27th, 2025

Today, I finished off my Falling Sand game!

- I created a while True loop that listens for events in Pygame (either QUIT or mouse click).
- I loop through the 80x80 grid to map out the location of all the water and sand blocks.
- I take user input and update the screen continuously.

---

## April 28th, 2025

For my final day, I spoke with the members of the current robotics coding team and had them take a look at my project.  
They evaluated my code and based on their feedback, they found it pretty good.  
I will now be submitting my project!
