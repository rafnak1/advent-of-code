#Clear time is the time it takes for a board to win
#check board is a boolean N x M matrix

#Returns a list of the sorted numbers

INPUT_FILE = 'input.txt'

def fetch_sorted_numbers():
    with open(INPUT_FILE) as f:
        a = f.read()
    a = a.split('\n')[0]
    a = a.split(',')
    a = list(map(int, a))
    return a

#Returns a list of integer matrices
def fetch_boards():
    with open(INPUT_FILE) as f:
        a = f.read()
    lines = a.split('\n')
    lines = lines[1:len(a)-1] 
    
    number_stream = []
    for line in lines:
        for number in line.split():
            number_stream.append(int(number))

    return fill_boards(number_stream)

#Receives a stream of integers
def fill_boards(stream):
    global N, M

    if len(stream) % N*M != 0:
        print('yabai!')
        return None

    bn = len(stream) // (N*M)
    boards = []
    for bi in range(bn):
        new_board = []
        for j in range(N):
            new_line = []
            for i in range(M):
                new_line.append(stream[bi*N*M + j*M + i])
            new_board.append(new_line)
        boards.append(new_board)

    return boards

#play the number on index i
def play(board, check_board, sni, sorted_numbers):
    global N,M
    for j in range(N):
        for i in range(M):
            if board[j][i] == sorted_numbers[sni]:
                check_board[j][i] = True

def compute_clear_time(board, sorted_numbers):
    i = -1
    check_board = [[False for i in range(M)] for j in range(N)]
    while(not is_win(check_board)):
        i += 1
        play(board, check_board, i, sorted_numbers)
    return i

def is_win(check_board):
    global N,M

    for j in range(N):
        if line_full(check_board, j):
            return True
    for i in range(M):
        if column_full(check_board, i):
            return True

    return False

def line_full(check_board, j):
    line = check_board[j]
    for square in line:
        if square == False:
            return False
    return True

def column_full(check_board, i):
    column = [check_board[j][i] for j in range(N)]
    for square in column:
        if square == False:
            return False
    return True

def index_of_smallest(int_array):
    for i in range(len(int_array)):
        if int_array[i] == min(int_array):
            return i

N,M = 5,5

sorted_numbers = fetch_sorted_numbers()
boards = fetch_boards()

clear_times = []

for board in boards:
    clear_times.append(compute_clear_time(board, sorted_numbers))

print(clear_times)
print(boards[index_of_smallest(clear_times)])

def get_sumof_unmarked_numbers(board, sorted_numbers):
    i = -1
    check_board = [[False for i in range(M)] for j in range(N)]
    while(not is_win(check_board)):
        i += 1
        play(board, check_board, i, sorted_numbers)
    
    r = 0
    for j in range(N):
        for i in range(M):
            if check_board[j][i] == False:
                r += board[j][i]

    return r

winboard = boards[index_of_smallest(clear_times)]
sum_of_unmarked_numbers = get_sumof_unmarked_numbers(winboard, sorted_numbers)

n = sorted_numbers[min(clear_times)]

print(sum_of_unmarked_numbers)
print(n)
print(n * sum_of_unmarked_numbers)

def index_of_greatest(int_array):
    for i in range(len(int_array)):
        if int_array[i] == max(int_array):
            return i

#now for the worst board:
loseboard = boards[index_of_greatest(clear_times)]
sum_of_unmarked_numbers = get_sumof_unmarked_numbers(loseboard, sorted_numbers)

n = sorted_numbers[max(clear_times)]

print(n * sum_of_unmarked_numbers)
