def read_file():
    with  open('input.txt', 'r') as reader:
        lines = reader.read().split('\n')[:-1]
    return lines

def run_cycles(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    depth = 3

    positions = [[['.' for x in range(rows)] for y in range(cols)] for z in range(depth)] 
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

input_face = read_file()
result = run_cycles(input_face)
print(result)
