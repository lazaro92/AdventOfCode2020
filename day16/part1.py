def read_input():
    with open('input.txt', 'r') as reader:
        lines = reader.read().split('\n')[:-1]
    return lines

def process(lines):
    ranges = []
    acc = 0
    for line in lines:
        if line == '':
            continue
        line_split = line.split(': ')
        if len(line_split) == 2: 
            for items in line_split[1].split(' or '):
                values = items.split('-')
                one_range = [int(values[0]), int(values[1])]
                ranges.append(one_range)
                continue
        line_split = line.split(',')
        if len(line_split) >= 2:
            for number in line_split:
                valid = False
                for mini, maxi in ranges:
                    number = int(number)
                    if mini <= number and number <= maxi:
                        valid = True
                        break
                if not valid:
                    acc += number
    return acc

input_lines = read_input()
result = process(input_lines)
print(result)
