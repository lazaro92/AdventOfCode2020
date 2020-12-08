def read_file():
    rd = open('input.txt', 'r')
    lines = rd.read().split('\n')[:-1]
    rd.close()
    return lines

def execute_program(instructions):
    acc = 0
    executed_lines = []

    x = 0
    while x not in executed_lines:
        executed_lines.append(x)
        current = instructions[x].split(' ')
        
        if current[0] == 'acc':
            acc += int(current[1])
            x += 1
        elif current[0] == 'jmp':
            x += int(current[1])
        elif current[0] == 'nop':
            x += 1
        else:
            print('instruction not found')
            return -1
    return acc

program = read_file()
accumulator = execute_program(program)

print(accumulator)

