def read_input():
    with open('input.txt', 'r') as reader:
        lines = reader.read().split('\n')[:-1]
    return lines

def process_program(lines):
    mask = 'X' * 36
    memory = dict()
    for line in lines:
        cmd, value = line.split(' = ')
        if cmd == 'mask':
            mask = value
        elif cmd[:3] == 'mem':
            address = extract_address(cmd[3:])
            binary = decimal_to_binary(int(value))
            for x in range(36):
                if mask[x] == '1' or mask[x] == '0':
                    binary = binary[:x] + mask[x] + binary[x+1:]
            memory[address] = binary
        else:
            return -1
    return memory

def extract_address(command):
    foundBegin = False
    address = ''
    for char in command:
        if char == '[':
            found_begin = True
        elif char == ']' and found_begin:
            return int(address)
        elif found_begin:
            address += char
    return -1

def decimal_to_binary(number):
    binary = ''
    if number == 0: return '0' * 36
    while number >= 1:
        binary = str(number % 2) + binary
        number //= 2
    return ('0' * (36 - len(binary))) + binary

def binary_to_decimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary // 10
        i += 1
    return decimal

program_lines = read_input()
mem = process_program(program_lines)

result = 0
for value in mem.values():
    result += binary_to_decimal(int(value))
print(result)
