import math

def find(data, min_val, max_val, char_range):
    if len(data) != 0:
        half = math.ceil((max_val - min_val) / 2.0) + min_val

        if data[0] == char_range[0]:
            return find(data[1:], min_val, half, char_range)
        elif data[0] == char_range[1]:
            return find(data[1:], half, max_val, char_range)
    return min_val

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text

text = read_file()

max_result = 0
for boarding_pass in text.split('\n'):
    row = find(boarding_pass[:7], 0, 127, 'FB')
    col = find(boarding_pass[7:], 0, 7, 'LR')

    result = row * 8 + col
    
    if result > max_result:
        max_result = result

print max_result
