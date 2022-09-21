# In progress

f = open("day9input.txt", "r")
data = f.readlines()
data = [list(map(int, data[x][:len(data[x])-1])) for x in range(len(data))]

sum_risk = 0
# corners
if (data[0][0] < data[0][1] and data[0][0] < data[1][0]):
    sum_risk += data[0][0] + 1
# top and bottom edge
for x in range(1, len(data[0])-1):
    y = len(data)-1
    if data[0][x] < data[1][x] and data[0][x] < data[0][x - 1] and data[0][x] < data[0][x + 1]:
        sum_risk += data[0][x]+1
    if data[y][x] < data[y - 1][x] and data[y][x] < data[y][x - 1] and data[y][x] < data[y][x + 1]:
        sum_risk += data[y][x]+1
# sides
for y in range(1, len(data)-1):
    x = len(data[0]) - 1
    if data[y][0] < data[y][1] and data[y][0] < data[y+1][0] and data[y][0] < data[y-1][0]:
        sum_risk += data[y][0] + 1
    #if data[y][x] < data[y][x-1] and data[y][x] < data[y-1][x] and data[y][x] < data[y+1][x]:
        #sum_risk += data[y][x] + 1
print(data[len(data)-2][len(data[0])-1])
# middle
for y in range(1, len(data)-1):
    for x in range(1, len(data[0])):
        if data[x][y] < data[x+1][y] and data[x][y] < data[x-1][y] and data[x][y] < data[x][y+1] and data[x][y] < data[x][y-1]:
            sum_risk += data[x][y] + 1
print(sum_risk)
