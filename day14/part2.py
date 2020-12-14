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
            binary_value = decimal_to_binary(int(value))
            binary_address = decimal_to_binary(int(address))
            addresses = process_save_data(mask, binary_address)
            x = 0
            for address in addresses:
                address = binary_to_decimal(int(address))
                memory[address] = binary_value
                x += 1
        else:
            return -1
    return memory

def process_save_data(mask, data, pos = 0):
    values = set()
    for x in range(pos, 36):
        if mask[x] == '1':
            data = data[:x] + mask[x] + data[x+1:]
        elif mask[x] == 'X':
            values.update(process_save_data(mask, data[:x] + '0' + data[x+1:], x+1))
            values.update(process_save_data(mask, data[:x] + '1' + data[x+1:], x+1))
    values.add(data) 
    return values


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
for address, value in mem.items():
    result += binary_to_decimal(int(value))
print(result)
