import math

def binary_find(data, min_val, max_val, char_range):
    if len(data) != 0:
        half = math.ceil((max_val + min_val) / 2.0)
        if data[0] == char_range[0]:
            return binary_find(data[1:], min_val, half, char_range)
        elif data[0] == char_range[1]:
            return binary_find(data[1:], half, max_val, char_range)
    return min_val

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text

text = read_file()
results = []
for boarding_pass in text.split('\n')[:-1]:
    row = binary_find(boarding_pass[:7], 0, 127, 'FB')
    col = binary_find(boarding_pass[7:], 0, 7, 'LR')
    results.append(row * 8 + col)

results.sort()
for x in range(1, len(results)-1): 
    if results[x] != results[x-1] +1 or results[x] != results[x+1] -1:
        print(results[x] + 1)
