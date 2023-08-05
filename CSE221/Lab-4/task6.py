inp = open('input6.txt', 'r')
out = open('output6.txt', 'w')

R, H = map(int, inp.readline().strip().split())

grid = []
for _ in range(R):
    row = list(inp.readline().strip())
    grid.append(row)

# print(grid)

def flood_fill(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '#':
        return 0

    diamonds = 0

    if grid[r][c] == 'D':
        diamonds += 1

    grid[r][c] = '#'

    diamonds += flood_fill(grid, r+1, c)
    diamonds += flood_fill(grid, r-1, c)
    diamonds += flood_fill(grid, r, c+1)
    diamonds += flood_fill(grid, r, c-1)

    return diamonds

max_diamonds = 0

for r in range(R):
    for c in range(H):
        if grid[r][c] == '.':
            diamonds = flood_fill(grid, r, c)
            max_diamonds = max(max_diamonds, diamonds)


out.write(str(max_diamonds))

inp.close()
out.close()