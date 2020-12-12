def read_file():
    numbers = [0]
    with  open('input.txt', 'r') as reader:
        for line in reader.read().split('\n')[:-1]:
            numbers.append(int(line))
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers

def process_jolts(jolts):
    diff1 = 0
    diff3 = 0
    for x in range(len(jolts)-1):
        if jolts[x+1] - jolts[x] == 3:
                diff3 += 1
        elif jolts[x+1] - jolts[x] == 2:
                continue
        elif jolts[x+1] - jolts[x] == 1:
                diff1 += 1
        else:
            return -1
    return diff1 * diff3

jolts = read_file()
result = process_jolts(jolts)
print(result)
