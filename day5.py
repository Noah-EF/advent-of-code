f = open('day5input.txt', 'r')
raw = f.readlines()
data = [[x.split()[0], x.split()[2]] for x in raw]

for line in range(0, len(data)):
    data[line] = [data[line][0].split(','), data[line][1].split(',')]

board = [[0 for x in range(0, 1000)] for y in range(0, 1000)]

for line in data:
    start_x = int(line[0][0])
    start_y = int(line[0][1])
    end_x = int(line[1][0])
    end_y = int(line[1][1])
    if start_x == end_x:
        for y in range(min(start_y, end_y), max(start_y, end_y)+1):
            board[y][start_x] += 1
    elif start_y == end_y:
        for x in range(min(start_x, end_x), max(start_x, end_x)+1):
            board[start_y][x] += 1
    else:
        length = abs(start_y-end_y)
        if start_y < end_y:
            # going down and to the right
            if start_x < end_x:
                for i in range(0, length+1):
                    board[start_y+i][start_x+i] += 1
            # going down and to the left
            else:
                for i in range(0, length+1):
                    board[start_y+i][start_x-i] += 1
        else:
            # going up
            if start_x < end_x:
                for i in range(0, length + 1):
                    board[start_y - i][start_x + i] += 1
            else:
                for i in range(0, length + 1):
                    board[start_y - i][start_x - i] += 1

total = 0

for row in range(0, 1000):
    for pt in range(0, 1000):
        if board[row][pt] >= 2:
            total += 1

print(total)
# not 14224, 14235, 14747 (low)
