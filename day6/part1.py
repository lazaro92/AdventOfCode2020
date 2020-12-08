def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text

def get_yes_answers_by_group(text):
    group_count = []
    answers = []
    for line in text.split('\n')[:-1]:
        if len(line) == 0:
            group_count.append(len(answers))
            answers = []
        else:
            for char in line:
                if char not in answers:
                    answers.append(char)
    group_count.append(len(answers))
    return group_count

text = read_file()
results = get_yes_answers_by_group(text)
print sum(results)
