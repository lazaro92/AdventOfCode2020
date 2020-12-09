def read_file():
    with  open('input.txt', 'r') as reader:
        numbers = [int(line) for line in reader.read().split('\n')[:-1]]
    return numbers

def find_set_that_sum_result(numbers, result):
    for x in range(len(numbers)):
        minim = numbers[x]
        maxim = numbers[x]
        acc = 0
        for y in range(x, len(numbers)):
            acc += numbers[y]
            if numbers[y] < minim:
                minim = numbers[y]
            elif numbers[y] > maxim:
                maxim = numbers[y] 
            if acc == result:
                return minim + maxim
    return -1

result = 26134589
numbers = read_file()
result = find_set_that_sum_result(numbers, result)
print(result)

