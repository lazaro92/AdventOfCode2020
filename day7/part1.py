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

def process_rules(dict_rules, bag_to_find='shiny gold'):
    possible_bags = set()
    for rules in dict_rules.items():
        for rule in rules[1]:
            if rule[1] == bag_to_find:
                possible_bags.add(rules[0])
                possible_bags.update(process_rules(dict_rules, rules[0]))
    return possible_bags

text = read_file()
dict_rules = create_dict(text)
result = process_rules(dict_rules)
print(len(result))
