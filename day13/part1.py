import math 

def read_input():
    with  open('input.txt', 'r') as reader:
        lines = reader.read().split('\n')[:-1]
    return lines

def find_near_bus(depart_time, buses):
    x = 0
    time = 0
    minim_time = math.inf
    minim_bus = 0
    while x < len(buses):
        time += buses[x]
        if time >= depart_time:
            if time < minim_time:
                minim_time = time
                minim_bus = x
            x += 1
            time = 0
    return (minim_time - depart_time) * buses[minim_bus]

input_lines = read_input()
buses = list(map(lambda x: int(x) , \
        filter(lambda x: x != 'x', input_lines[1].split(','))))

result = find_near_bus(int(input_lines[0]), buses)
print(result)

