# seems like linear regression?
# definitely minimization with one parameter (but not cost minimization)
# maybe try to regress to fuel = 0 at all points? have to make sure its not least squares though
f = open("day7input.txt", "r")
data = list(map(int, f.read().split(',')))
max_pos = max(data)
min_pos = min(data)
fuel_usage = []
for p in range(min_pos, max_pos):
    fuel_nums = []
    for x in data:
        fuel_nums.append(x-p)
    fuel_usage.append(sum(fuel_nums))
print(min(fuel_nums))

# not 1954, too low