f = open("day3input.txt", 'r')
start_data = f.read().splitlines()
i = 0
def the_thing(data, i):
    count = 0
    new_data = []
    for x in data:
        if x[i] == '1':
            count +=1
    if count >= len(data)/2:
        num = '1'
    else:
        num = '0'
    for x in data:
        if x[i] == num:
            new_data.append(x)
    if len(new_data)==1:
        return new_data
    return the_thing(new_data, i+1)

def the_other_thing(data, i):
    count = 0
    new_data = []
    for x in data:
        if x[i] == '1':
            count +=1
    if count < len(data)/2:
        num = '1'
    else:
        num = '0'
    for x in data:
        if x[i] == num:
            new_data.append(x)
    if len(new_data)==1:
        return new_data
    return the_other_thing(new_data, i+1)

co2 = int(''.join(list(map(str, the_other_thing(start_data, i)))), 2)
oxy = int(''.join(list(map(str, the_thing(start_data, i)))), 2)
print(oxy)
print(co2)
print(co2*oxy)
