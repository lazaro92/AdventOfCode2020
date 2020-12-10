def read_file():
    numbers = [0]
    max_num = 0
    with  open('input.txt', 'r') as reader:
        for line in reader.read().split('\n')[:-1]:
            number = int(line)
            numbers.append(number)

            if (number > max_num):
                max_num = number
    numbers.append(max_num + 3)
    return numbers

def process_jolts(jolts):
    x = 0
    diff1 = 0
    diff3 = 0
    for x in range(len(jolts)):
        if x + 1 == len(jolts):
            break

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
jolts.sort()
result = process_jolts(jolts)
print(result)
