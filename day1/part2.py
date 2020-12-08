def operateNumbers(numbers):
    results = []
    length = len(numbers)
    for x in range(length):
        for y in range(x, length):
            for z in range(y, length):
                if (numbers[x] + numbers[y] + numbers[z])  == SUM_RESULT:
                    results.append([numbers[x], numbers[y], numbers[z]])
    return results

def readFile():
    numbers = []
    rd = open('input.txt', 'r')
    while True:
        line = rd.readline()
        if not line:
            break;
        numbers.append(int(line))
    rd.close()

    return numbers

def printResults(results):
    if len(results) == 0:
        print('No results')
    else:
        for result in results:
            print(result[0] * result[1] * result[2])

SUM_RESULT = 2020
numbers = readFile()
results = operateNumbers(numbers)
printResults(results)
