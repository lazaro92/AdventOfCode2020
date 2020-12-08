def count_trees(data, col, row, count):
    col_max = len(data[0])
    row_max = len(data)
    if col >= col_max:
        col = col - col_max 
    if row < row_max:
        if data[row][col] == '#':
            count += 1
        return count_trees(data, col+3, row+1, count)
    return count

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
        
    rd.close()
    return text.split('\n')[:-1]

data = read_file()
result = count_trees(data, 0, 0, 0)
print('Number of trees: ', result)
