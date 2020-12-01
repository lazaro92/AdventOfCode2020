# find the two entries that sum to 2020 and then multiply those two numbers together.
# For example, 1721 and 299 sums 2020

def operateNumbers(numbers):

    length = len(numbers)
    pairs = []
    for x in range(length):
        for y in range(length):
            if numbers[x] + numbers[y] == SUM_RESULT:
                pairs.append((numbers[x], numbers[y]))
    return pairs


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
    for result in results:
        print(str(result[0]) +  " * " +  str(result[1]) + " = " + str(result[0] * result[1]))

SUM_RESULT = 2020
numbers = readFile()
results = operateNumbers(numbers)
printResults(results)
