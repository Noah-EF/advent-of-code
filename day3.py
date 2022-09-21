f = open("day3input.txt", 'r')
data = f.read().splitlines()
# count of 1's 
count = [0 for x in range(0, len(data[0]))]
for x in data:
    for digit in range(0, len(x)):
        if x[digit] == '1':
            count[digit] += 1
gamma = [(1 if count[x]>len(data)/2 else 0) for x in range(0, len(count))]
epsilon = [(1 if gamma[x] == 0 else 0) for x in range(0, len(count))]
gamma = int(''.join(list(map(str, gamma))), 2)
epsilon = int(''.join(list(map(str, epsilon))), 2)
print(gamma*epsilon)




