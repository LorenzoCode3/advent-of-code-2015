import os
import copy

def create_grid():
    grid = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    corners = [(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)]
    for x, y in corners:
        grid[x][y] = '#'
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def get_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1), (1, 0), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    live_neighbors = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '#':
            live_neighbors += 1
    return live_neighbors

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = copy.deepcopy(grid)
    
    for x in range(rows):
        for y in range(cols):
            live_neighbors = get_neighbors(grid, x, y)
            if grid[x][y] == '#' and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[x][y] = '.'
            elif grid[x][y] == '.' and live_neighbors == 3:
                new_grid[x][y] = '#'

    corners = [(0, 0), (0, len(new_grid[0]) - 1), (len(new_grid) - 1, 0), (len(new_grid) - 1, len(new_grid[0]) - 1)]
    for x, y in corners:
        new_grid[x][y] = '#'
    return new_grid

def game_of_life(generations):
    grid = create_grid()
    
    for generation in range(generations):
        grid = next_generation(grid)
    
    count_on = sum(row.count('#') for row in grid)
    print("Cells that are 'on':", count_on)

game_of_life(100)