import math
def expand_grid(grid):
    row_star = [any(cell == '#' for cell in row) for row in grid]#checking row for star(this is basically nested loop)
    column_star = [any(grid[row][col] == '#' for row in range(len(grid))) for col in range(len(grid[0]))]#checking column for star
    expanded_grid = []
    for i, row in enumerate(grid):#expanding through rows
        if not row_star[i]:
            expanded_grid.append(row)
        expanded_grid.append(row)
    final_expanded_grid = []
    for row in expanded_grid:#exxpanding through column
        new_row = []
        for j, cell in enumerate(row):
            if not column_star[j]:
                new_row.append(cell)
            new_row.append(cell)
        final_expanded_grid.append(new_row)
    return final_expanded_grid
def dist(expanded_grid):
    star = []
    for y, row in enumerate(expanded_grid):#storing the coordinates as tuples
        for x, cell in enumerate(row):
            if cell == '#':
                star.append((x, y))
    distances = []
    for i in range(len(star)):#calculating distances between all possible pairs
        for j in range(i + 1, len(star)):
            x1, y1 = star[i]
            x2, y2 = star[j]
            distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            distances.append(distance)
    return min(distances), max(distances)
grid = []
for _ in range(10):
    grid.append(list(input().strip()))
expanded_grid = expand_grid(grid)
min_dist, max_dist =dist(expanded_grid)
min_result=math.floor(min_dist)
max_result=math.floor(max_dist)
print(min_result, max_result)
