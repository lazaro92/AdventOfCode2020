def read_file():
    with  open('input.txt', 'r') as reader:
        lines = reader.read().split('\n')[:-1]
    return lines

def evaluate(expression):
    operator = ''
    current = 0
    prev_value = ''

    index = 0
    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            prev_value += char

        elif char in '+*':
            # prev value eval
            if operator != '':
                if operator == '+':
                    current += int(prev_value)
                else:
                    current *= int(prev_value)
            else:
                # get first value
                current = int(prev_value)

            prev_value = ''
            operator = char

        elif char == '(':
            # Balance the parentheses to get to the end
            ls = 1 # Lefts
            rs = 0 # Rights
            startIndex = index + 1

            while ls != rs and index < len(expression):
                index += 1
                ls += expression[index] == '('
                rs += expression[index] == ')'

            # Lefts and rights are balanced, evaluate what's inside
            insideParentheses = expression[startIndex:index]
            prev_value = evaluate(insideParentheses)

        index += 1

    # At the end, perform the last operation
    if operator != '':
        if operator == '+':
            current += int(prev_value)
        else:
            current *= int(prev_value)

    return current

ans = 0
for expression in read_file():
    expression = expression.replace(' ', '')
    ans += evaluate(expression)
print(ans)
