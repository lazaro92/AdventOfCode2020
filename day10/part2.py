def read_file():
    numbers = [0]
    max_num = 0
    with  open('input2.txt', 'r') as reader:
        for line in reader.read().split('\n')[:-1]:
            number = int(line)
            numbers.append(number)

            if (number > max_num):
                max_num = number
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers

def count_combinations(jolts, y=0):
    count = 1
    for x in range(len(jolts) - 1):
        if jolts[x+1] - jolts[x] == 3:
            continue
        elif(jolts[x+1] - jolts[x] == 1):
            count += count_combinations(jolts[:x+1] + jolts[x+3:], x)
        elif (jolts[x+1] - jolts[x] == 2):
            count += count_combinations(jolts[:x+1] + jolts[x+2:], x)
        else:
            return 0
    print(jolts, y)
    return count

jolts = read_file()
result = count_combinations(jolts)
print(result)
