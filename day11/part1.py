def read_file():
    with  open('input.txt', 'r') as reader:
        matrix = [[char for char in line] for line in reader.read().split('\n')[:-1]]
    return matrix

def process(matrix):
    positions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]
    new_matrix = [row[:] for row in matrix]
    has_changed = False
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == '.':
                continue
            elif matrix[row][col] == 'L':
                no_occupied_adjacents = True
                for posX, posY in positions:
                    if (row + posX >= 0) and (row + posX < len(matrix)) and \
                    (col + posY >= 0) and (col + posY < len(matrix[0])):
                        if matrix[row + posX][col + posY] == '#':
                            no_occupied_adjacents = False
                if no_occupied_adjacents:
                    new_matrix[row][col] = '#'
                    has_changed = True
            elif matrix[row][col] == '#':
                adjacent = 0
                for posX, posY in positions:
                    if (row + posX >= 0) and (row + posX < len(matrix)) and \
                    (col + posY >= 0) and (col + posY < len(matrix[0])):
                        if matrix[row + posX][col + posY] == '#':
                            adjacent += 1
                if adjacent >= 4:
                    new_matrix[row][col] = 'L'
                    has_changed = True
            else:
                return -1
    return new_matrix, has_changed

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
