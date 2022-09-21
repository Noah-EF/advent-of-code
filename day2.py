f = open("day2input.txt", "r")
commands = f.read().split()
increment = [commands[2*x+1] for x in range(0, len(commands)//2)]
com = [commands[2*x] for x in range(0, len(commands)//2)]
p = 0
d = 0
for x in range(0, len(com)):
    if com[x] == 'forward':
        p += int(increment[x])
    if com[x] == 'down':
        d += int(increment[x])
    if com[x] == 'up':
        d -= int(increment[x])
p = 0
d = 0
a = 0

for x in range(0, len(com)):
    if com[x] == 'forward':
        p += int(increment[x])
        d += int(increment[x])*a
    if com[x] == 'down':
        a += int(increment[x])
    if com[x] == 'up':
        a -= int(increment[x])
print(p*d)
