# Solution obtained in Reddit

def read_file():
    numbers = [0]
    with  open('input.txt', 'r') as reader:
        for line in reader.read().split('\n')[:-1]:
            numbers.append(int(line))
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers

def count_combinations(jolts):
    count = 1
    ones = 0
    for x in range(len(jolts) - 1):
        if jolts[x+1] - jolts[x] == 1:
            ones += 1
        else:
            if ones > 1:
                if ones == 2:
                    count *= 2
                elif ones == 3:
                    count *= 4
                elif ones == 4:
                    count *= 7
            ones = 0
    return count

jolts = read_file()
result = count_combinations(jolts)
print(result)
