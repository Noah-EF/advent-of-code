f = open("day1input.txt", "r")
num = f.read().split()
num = list(map(int, num))
print(num)
inc = 0
for x in range(1, len(num)):
    if num[x]>num[x-1]:
        inc +=1
print(inc)

threesum = [num[x]+num[x+1]+num[x+2] for x in range(0, len(num)-2)]
print(threesum)
inc = 0
for x in range(1, len(threesum)):
    if threesum[x]>threesum[x-1]:
        inc +=1
print(inc)
