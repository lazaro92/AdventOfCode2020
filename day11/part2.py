def read_file():
    with  open('input.txt', 'r') as reader:
        matrix = [[char for char in line] for line in reader.read().split('\n')[:-1]]
    return matrix

def process(matrix):
    new_matrix = [row[:] for row in matrix]
    has_changed = False
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '.':
                continue
            elif matrix[row][col] == 'L':
                if find_occupied_in_left_direction(matrix,row,col) == 0 and \
                find_occupied_in_right_direction(matrix,row,col) == 0 and \
                find_occupied_in_upper_direction(matrix,row,col) == 0 and \
                find_occupied_in_lower_direction(matrix,row,col) == 0 and \
                find_occupied_in_right_upper_direction(matrix,row,col) == 0 and \
                find_occupied_in_right_lower_direction(matrix,row,col) == 0 and \
                find_occupied_in_left_lower_direction(matrix,row,col) == 0 and \
                find_occupied_in_left_upper_direction(matrix,row,col) == 0: 
                    new_matrix[row][col] = '#'
                    has_changed = True
            elif matrix[row][col] == '#':
                count = 0
                if find_occupied_in_left_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_right_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_upper_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_lower_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_right_upper_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_right_lower_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_left_lower_direction(matrix,row,col) == 1:
                    count += 1
                if find_occupied_in_left_upper_direction(matrix,row,col) == 1:
                    count += 1
                if count >= 5:
                    new_matrix[row][col] = 'L'
                    has_changed = True
            else:
                return -1
    return new_matrix, has_changed

def find_occupied_in_left_direction(matrix, row, col):
    col -=1
    while col >= 0:
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        col -= 1
    return 0

def find_occupied_in_right_direction(matrix, row, col):
    col += 1
    while col < len(matrix[0]):
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        col += 1
    return 0

def find_occupied_in_upper_direction(matrix, row, col):
    row -= 1
    while row >= 0:
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row -= 1
    return 0

def find_occupied_in_lower_direction(matrix, row, col):
    row += 1
    while row < len(matrix):
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row += 1
    return 0

def find_occupied_in_left_upper_direction(matrix, row, col):
    row -= 1
    col -= 1
    while row >= 0 and col >= 0:
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row -= 1
        col -= 1
    return 0

def find_occupied_in_right_upper_direction(matrix, row, col):
    row -= 1
    col += 1
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row -= 1
        col += 1
    return 0

def find_occupied_in_left_lower_direction(matrix, row, col):
    row += 1
    col -= 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row += 1
        col -= 1
    return 0

def find_occupied_in_right_lower_direction(matrix, row, col):
    row += 1
    col += 1
    while row < len(matrix) and col < len(matrix[0]):
        if matrix[row][col] == 'L':
            return 0
        elif matrix[row][col] == '#':
            return 1
        row += 1
        col += 1
    return 0

def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            print(matrix[x][y], end='')
        print('\n', end='')

def count_occupied_seats(matrix):
    occupied_seats = 0
    for row in matrix:
        for char in row:
            if char == '#':
                occupied_seats += 1
    return occupied_seats

matrix = read_file()
while True:
    matrix, changed = process(matrix)
    if not changed: break
print(count_occupied_seats(matrix))
