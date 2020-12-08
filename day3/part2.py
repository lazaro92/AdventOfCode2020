def count_trees(data, col, row, count):
    col_max = len(data[0])
    row_max = len(data)
    if col >= col_max:
        col = col - col_max 
    if row < row_max:
        if data[row][col] == '#':
            count += 1
        return count_trees(data, col + col_slope, row + row_slope, count)
    return count

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text.split('\n')[:-1]

slopes_movement = [[1,1], [3,1], [5,1], [7,1], [1,2]]
counts = []
i = 0

data = read_file()

for i in range(len(slopes_movement)):
    col_slope = slopes_movement[i][0]
    row_slope = slopes_movement[i][1]
    result = count_trees(data, 0, 0, 0)
    counts.append(result)

print('Result: ', reduce((lambda x, y: x * y), counts))
