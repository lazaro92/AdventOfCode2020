def read_file():
    rd = open('input.txt', 'r')
    lines = rd.read().split('\n')[:-1]
    rd.close()
    return lines

def execute_program(instructions):
    acc = 0
    executed_lines = []

    x = 0
    while x < len(instructions):
        if x in executed_lines:
            return -1
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

def find_correct_acc(program):
    for x in range(len(program)):
        swap = False
        swap = swap_instruction(program, x)

        accumulator = execute_program(program)
        if accumulator != -1:
            return accumulator

        if swap == True:
            swap = swap_instruction(program, x)

def swap_instruction(program, line):
    swap = False
    instruction = program[line].split(' ')
    if instruction[0] == 'jmp':
        program[line] = 'nop ' + instruction[1]
        swap = True
    elif instruction[0] == 'nop':
        program[line] = 'jmp ' + instruction[1]
        swap = True
    return swap

program = read_file()
real_accumulator = find_correct_acc(program)
print(real_accumulator)
