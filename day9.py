# In progress
# part 1 done
# part 2 will use variation of Dijkstra's algorithm
f = open("day9input.txt", "r")
raw_data = f.readlines()
data = []
for y in range(len(raw_data)):
    line = []
    for x in range(len(raw_data[0]) - 1):
        line.append(int(raw_data[y][x]))
    data.append(line)
# print(*data, sep='\n')
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
# should y and x be switched?
for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        if data[x][y] < data[x + 1][y] and data[x][y] < data[x - 1][y] and data[x][y] < data[x][y + 1] \
                and data[x][y] < data[x][y - 1]:
            sum_risk += data[x][y] + 1
print(sum_risk)

# part 2
# treating 9 as barriers
# need to find the largest bound areas

basins = []
checked_coordinates = []
count = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        # skip coordinates that have been already checked or are borders (9)
        if (y, x) in checked_coordinates or data[y][x] == 9:
            pass
        else:
            basin = []
            to_check = [(y, x)]
            while len(to_check) > 0:
                # if first item in to_check list is a 9, remove from to check list
                # print(to_check)
                if data[to_check[0][0]][to_check[0][1]] == 9 or to_check[0] in checked_coordinates:
                    checked_coordinates.append(to_check[0])
                    to_check.pop(0)
                else:
                    # attempt to add all adjacent squares to to_check
                    # if index is out of bounds, will not be added
                    basin.append(to_check[0])
                    if (to_check[0][0] + 1, to_check[0][1]) not in checked_coordinates and \
                                (to_check[0][0] + 1 < 100 and to_check[0][1] < 100) and \
                                (to_check[0][0] + 1 >= 0 and to_check[0][1] >= 0):
                        to_check.append((to_check[0][0] + 1, to_check[0][1]))

                    if (to_check[0][0] - 1, to_check[0][1]) not in checked_coordinates and \
                                (to_check[0][0] - 1) < 100 and to_check[0][1] < 100 and \
                                (to_check[0][0] - 1) >= 0 and to_check[0][1] >= 0:
                        to_check.append((to_check[0][0] - 1, to_check[0][1]))

                    if (to_check[0][0], to_check[0][1] + 1) not in checked_coordinates and \
                            to_check[0][0] < 100 and (to_check[0][1] + 1) < 100 and \
                            to_check[0][0] >= 0 and (to_check[0][1] + 1) >= 0:
                        to_check.append((to_check[0][0], to_check[0][1] + 1))

                    if (to_check[0][0], to_check[0][1] - 1) not in checked_coordinates and \
                            to_check[0][0] < 100 and (to_check[0][1] - 1) < 100 and \
                            to_check[0][0] >= 0 and (to_check[0][1] - 1) >= 0:
                        to_check.append((to_check[0][0], to_check[0][1] - 1))
                    checked_coordinates.append(to_check[0])
                    to_check.pop(0)
            basins.append(basin)
lengths = [len(x) for x in basins]
lengths.sort()
print(lengths[len(lengths)-3:])
print(93*94*98)