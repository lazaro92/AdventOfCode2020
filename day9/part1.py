def read_file():
    with  open('input.txt', 'r') as reader:
        numbers = [int(line) for line in reader.read().split('\n')[:-1]]
    return numbers

def find_rebel_number(numbers, preamble):
    x = 0
    found = False
    init = 0
    while x < len(numbers):
        for y in range(x+1, preamble):
            if (numbers[x] + numbers[y]) == numbers[preamble]:
                found = True
                break    
        if x == preamble:
            if found:
                preamble += 1 
                init += 1
                x = init
                found = False
            else:
                return numbers[x]
        else:
            x += 1
    return -1

preamble = 25
numbers = read_file()
number = find_rebel_number(numbers, preamble)
print(number)

