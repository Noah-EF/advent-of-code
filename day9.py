# In progress
# part 1 done

f = open("day9input.txt", "r")
raw_data = f.readlines()
data = []
for y in range(len(raw_data)):
    line = []
    for x in range(len(raw_data[0]) - 1):
        line.append(int(raw_data[y][x]))
    data.append(line)
print(*data, sep='\n')
sum_risk = 0
# corners
# top left
if data[0][0] < data[0][1] and data[0][0] < data[1][0]:
    sum_risk += data[0][0] + 1
# top right
if data[0][len(data[0]) - 1] < data[0][len(data[0]) - 2] and data[1][len(data[0]) - 1]:
    sum_risk += data[0][len(data[0]) - 1] + 1
# bottom left
if data[len(data) - 1][0] < data[len(data) - 1][1] and data[len(data) - 1][0] < data[len(data) - 2][0]:
    sum_risk += data[len(data) - 1][0] + 1
# bottom right
if data[len(data) - 1][len(data[0]) - 1] < data[len(data) - 2][len(data[0]) - 1] and data[len(data) - 1][
    len(data[0]) - 1] < data[len(data) - 1][len(data[0]) - 2]:
    sum_risk += data[len(data) - 1][len(data[0]) - 1] + 1
# top and bottom edge
for x in range(1, len(data[0]) - 1):
    y = len(data) - 1
    if data[0][x] < data[1][x] and data[0][x] < data[0][x - 1] and data[0][x] < data[0][x + 1]:
        sum_risk += data[0][x] + 1
    if data[y][x] < data[y - 1][x] and data[y][x] < data[y][x - 1] and data[y][x] < data[y][x + 1]:
        sum_risk += data[y][x] + 1
# sides
for y in range(1, len(data) - 1):
    x = len(data[0]) - 1
    if data[y][0] < data[y][1] and data[y][0] < data[y + 1][0] and data[y][0] < data[y - 1][0]:
        sum_risk += data[y][0] + 1
    if data[y][x] < data[y][x - 1] and data[y][x] < data[y - 1][x] and data[y][x] < data[y + 1][x]:
        sum_risk += data[y][x] + 1
print(data[len(data) - 2][len(data[0]) - 1])
# middle
for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        if data[x][y] < data[x + 1][y] and data[x][y] < data[x - 1][y] and data[x][y] < data[x][y + 1] \
                and data[x][y] < data[x][y - 1]:
            sum_risk += data[x][y] + 1
print(sum_risk)
