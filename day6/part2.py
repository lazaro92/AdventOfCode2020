def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text

def get_yes_answers_by_group(text):
    group_count = []
    answers = {}
    persons = 0
    for line in text.split('\n')[:-1]:
        if len(line) == 0:
            count = len(filter(lambda x: x == persons, answers.values()))
            group_count.append(count)
            answers = {}
            persons = 0
        else:
            for char in line:
                if answers.get(char) == None:
                    answers[char] = 1
                else:
                    answers[char] += 1
            persons += 1
    count = len(filter(lambda x: x == persons, answers.values()))
    group_count.append(count)
    return group_count

text = read_file()
results = get_yes_answers_by_group(text)
print(sum(results))
