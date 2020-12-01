def operateNumbers(numbers):
    length = len(numbers)
    for x in range(length):
        for y in range(length):
            for z in range(length):
                if (numbers[x] + numbers[y] + numbers[z])  == SUM_RESULT:
                    return [numbers[x], numbers[y], numbers[z]]
            


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

def printResults(result):
    if len(result) == 0:
        print('No results')
    else:
        print(str(result[0]) +  " * " +  str(result[1]) + " * " + str(result[2]) + " = " + str(result[0] * result[1] * result[2]))

SUM_RESULT = 2020
numbers = readFile()
result = operateNumbers(numbers)
printResults(result)
