f = open("day11input.txt", "r")
raw_data = f.readlines()
data = []
for y in range(len(raw_data)):
    line = []
    for x in range(len(raw_data[0]) - 1):
        line.append(int(raw_data[y][x]))
    data.append(line)
# print(*data, sep='\n')
# part 1:
# first try: 1716, too low
# second try: 1743, correct
# problem was putting >= 9 instead of > 9
count = 0


def step(grid):
    # 2d list of octopuses, 1 indicates didn't flash this time, 0 indicates flashed
    global count
    flashed = [[1 for _ in range(10)] for _ in range(10)]
    # add 1 to each
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
    done = False
    while not done:
        done = True
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if flashed[y][x] == 1 and grid[y][x] > 9:
                    flashed[y][x] = 0
                    count += 1
                    done = False
                    # all adjacent squares including diagonals
                    for (i, j) in [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, 1), (-1, -1)]:
                        if 0 <= y + i < len(grid) and 0 <= x + j < len(grid[0]):
                            grid[y + i][x + j] += 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] *= flashed[y][x]

# part 2:
# first guess 364, correct
for x in range(1000):
    step(data)
    success = True
    for y in range(len(data)):
        for z in range(len(data[0])):
            if data[y][z] != 0:
                success = False
    if success:
        print(x + 1)
        break
