def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
    rd.close()
    return text

def create_dict(text):
    colors = {}
    for line in text.split('\n')[:-1]:
        words = line.split(' ') 
        
        key_color = ' '.join(words[:2])
        colors[key_color] = []
        
        if words[4] == 'no':
            continue
        for x in range(line.count(',') + 1):
            position = x * 4 + 4
            temp = [int(words[position]), ' '.join(words[position + 1:position + 3])]
            colors[key_color].append(temp)
    return colors

def process_data(all_rules, current_bag, find_bag):
    found = False
    for rule in all_rules[current_bag]:
        if find_bag in rule[1]:
            return True
        else: 
            found = process_data(all_rules, rule[1], find_bag)
    return found

text = read_file()
rules = reformat(text)

count = 0
for bag in rules.keys():
    result = process_data(rules, bag, 'shiny gold')
    if result: count += 1

print(count)
