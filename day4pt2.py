import copy
f = open('day4input.txt', 'r')
data = f.read().splitlines()
drawn = data[0]
drawn = list(map(int, drawn.split(',')))
boards = data[1:]
boards_processed = []
# list where 0 indicated corresponding board has not won yet
for x in range(0, len(boards)//6):
    boards_processed.append([list(map(int,boards[6*x+1].split())),
                             list(map(int, boards[6*x+2].split())),
                             list(map(int, boards[6*x+3].split())),
                             list(map(int, boards[6*x+4].split())),
                             list(map(int, boards[6*x+5].split()))])

boards_left = [0 for x in range(0, len(boards_processed))]
empty_board = [[0 for x in range(0, 5)]for x in range(0, 5)]
marked = [copy.deepcopy(empty_board) for x in boards_processed]

def play_num(drawn_num):
    for board in range(0, len(boards_processed)):
        for row in range(0, 5):
            for col in range(0, 5):
                if boards_processed[board][row][col] == drawn_num:
                    marked[board][row][col] = 1
    return check_win(boards_processed, marked, drawn_num)

def check_win(boards_processed, marked, last_num):
    found = False
    for x in range(0, len(boards_processed)):
        if check_board(boards_processed[x], marked[x], last_num):
            boards_left[x] = 1
            found = True
    if found:
        return check_board(boards_processed[x], marked[x], last_num)
    return False

def check_board(board, marks, last_num):
    #check each row
    for row in range(0, 5):
        if (marks[row][0]!=0 and marks[row][1]!=0 and marks[row][2]!=0 and marks[row][3]!=0 and marks[row][4]!=0):
            return win(board, marks, last_num)
    for x in range(0, 5):
        if marks[0][x]!=0 and marks[1][x]!=0 and marks[2][x]!=0 and marks[3][x]!=0 and marks[4][x]!=0:
            return win(board, marks, last_num)
    return False

def win(board, marks, last_num):
    sum = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if marks[x][y]==0:
                sum+=board[x][y]
    return sum*last_num


for num in drawn:
    play_num(num)
    # not getting run for some reason
    if boards_left.count(0) == 1:
        b = boards_processed[boards_left.index(0)]
        m = marked[boards_left.index(0)]
        for x in drawn[drawn.index(num)+1:]:
            for row in range(0, 5):
                for col in range(0, 5):
                    if b[row][col] == x:
                        m[row][col] = 1
            if check_board(b, m, x):
                print(check_board(b, m, x))
                break
        '''total = 0
        for row in range(0, 5):
            for col in range(0, 5):
                if m[row][col] == 0:
                    total += b[row][col]
        print("Answer: ", end = '')
        print(total*num)'''