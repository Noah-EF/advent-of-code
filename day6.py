import sys

f = open("day6input.txt", "r")
data = list(map(int, f.read().split(',')))

def one_day(fish):
    fish = [x - 1 for x in fish]
    new_fish = fish.count(-1)
    fish = [x if x>=0 else 6 for x in fish]
    for i in range(new_fish):
        fish.append(8)
    return fish

# resulting values after 64 days
resulting_values = {}
# if we split to 128, 128 might not need to remember list only size?
for num in range(9):
    i = [num]
    for x in range(128):
        i = one_day(i)
    resulting_values[num] = len(i)
print("Single Input results collected")
'''for num in range(9):
    print(len(resulting_values[num]))'''
for x in range(128):
    data = one_day(data)
print("First 128 days calculated")
counts = []
for x in range(9):
    counts.append(data.count(x))
print(counts)
data.clear()
sum = 0
for x in range(9):
    try:
        sum += counts[x]*resulting_values[x]
    except: print(x)
print(sum)


