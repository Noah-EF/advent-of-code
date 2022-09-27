f = open("day10input.txt", "r")
data = f.readlines()
error = 0

# score incomplete line for part 2
# part 2:
# guess 1: 770783, too low
# guess 2: 820045242, correct
# problem was indentation issue in loop
scores = []


def score(l):
    s = 0
    l.reverse()
    for c in l:
        s *= 5
        if c == '(':
            s += 1
        if c == '[':
            s += 2
        if c == '{':
            s += 3
        if c == '<':
            s += 4
    scores.append(s)


# part 1:
# first guess: 1010181, too high
# second guess: 288291, correct
# problem was not stopping once first incorrect character was found on line
for line in data:
    buffer = [line[0]]
    corrupted = False
    for c in line[1:-1]:
        if (buffer[-1] == '(' and c == ')') or (buffer[-1] == '[' and c == ']') or \
                (buffer[-1] == '{' and c == '}') or (buffer[-1] == '<' and c == '>'):
            buffer.pop()
        elif c == ')':
            error += 3
            corrupted = True
            break
        elif c == ']':
            error += 57
            corrupted = True
            break
        elif c == '}':
            error += 1197
            corrupted = True
            break
        elif c == '>':
            error += 25137
            corrupted = True
            break
        else:
            buffer.append(c)
    if not corrupted:
        score(buffer)
print(error)
scores.sort()
print(len(scores))
print(scores[len(scores) // 2])
