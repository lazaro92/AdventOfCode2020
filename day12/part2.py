def read_file():
    with  open('input.txt', 'r') as reader:
        instructions = [[line[0],int(line[1:])] for line in reader.read().split('\n')[:-1]]
    return instructions

def get_manhattan_distace(instructions):
    x = 0
    y = 0
    wp_x = 10
    wp_y = -1
    facing = 90
    for command, value in instructions:
        if command == 'N': wp_y -= value
        elif command == 'S': wp_y += value
        elif command == 'E': wp_x += value
        elif command == 'W': wp_x -= value
        elif command == 'L':
            wp_x, wp_y = rotate(( 360 + value) % 360, wp_x, wp_y)
        elif command == 'R':
            wp_x, wp_y = rotate(( 360 - value) % 360, wp_x, wp_y)
        elif command == 'F':
            x += wp_x * value
            y += wp_y * value
    return abs(x) + abs(y)

def rotate(grades, wp_x, wp_y):
    if grades == 90:
        temp_x = wp_x
        wp_x = wp_y
        wp_y = -temp_x
    if grades == 180:
        wp_y = -wp_y 
        wp_x = -wp_x
    if grades == 270:
        temp_x = wp_x
        wp_x = -wp_y
        wp_y = temp_x
    if grades == 0:
        wpy = wpy
        wpx = wpx
    return [wp_x, wp_y]

instructions = read_file()
distance = get_manhattan_distace(instructions)
print(distance)
