def read_file():
    with  open('input.txt', 'r') as reader:
        instructions = [[line[0],int(line[1:])] for line in reader.read().split('\n')[:-1]]
    return instructions

def get_manhattan_distace(instructions):
    x = 0
    y = 0
    facing = 90
    for command, value in instructions:
        if command == 'N': y -= value
        elif command == 'S': y += value
        elif command == 'E': x += value
        elif command == 'W': x -= value
        elif command == 'L': facing = (360 + facing - value) % 360
        elif command == 'R': facing = (360 + facing + value) % 360
        elif command == 'F':
            if facing == 90: x += value
            elif facing == 180: y += value
            elif facing == 270: x -= value
            elif facing == 0: y -= value
    return abs(x) + abs(y)

instructions = read_file()
distance = get_manhattan_distace(instructions)
print(distance)
