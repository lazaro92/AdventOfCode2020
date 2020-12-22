def structure_data(data):
    result = []
    for x in data:
        num = x[0].split(' ')[1][:-1]
        result.append([int(num), x[1:]])
    return result

data = [x.splitlines() for x in open('input1.txt', 'r').read().split('\n\n')]
data = structure_data(data)

for id, block in data:
    print(id, block)
