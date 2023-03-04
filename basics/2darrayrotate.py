
grid1 = [[9,9,1,1],
        [8,8,1,1],
        [1,1],
        [1,1,1,1]]

grid2 = [[1,1,1,1,1,1],
         [1,1,1,1,1,1],
         [1,2,1,1,1,1],
         [1,1,1,1,1,1],
         [1,2,1,1,1,2],
         [1,1,1,2,1,1]]

def new_grid(grid):
    new_grid = []
    for x in range(0, len(grid), 1):
        new_list = []
        for y in range(len(grid)-1, -1, -1):
            new_list.append(grid[y][x])
        new_grid.append(new_list)
    return new_grid

def grid_check(grid):
    for x in range(0, len(grid), 1):
        y = len(grid)
        if not len(grid[x]) == y:
            return False

def print_grid (grid):
    if grid == None:
        print("Not a grid")
        return
    for y in grid:
        for x in y:
            print(x, end=' ')
        print()

def rotate90(grid,no_rot):
    if grid_check(grid) == False:
        print("Not a square grid")
        return
    no_rot %= 4
    while no_rot > 0:
        grid = new_grid(grid)
        no_rot -= 1
    return grid

x = rotate90(grid1, 6)
print_grid(x)