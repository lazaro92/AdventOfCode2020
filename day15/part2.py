def read_input():
    with open('input.txt', 'r') as reader:
        numbers = [int(x) for x in reader.read().split(',')]
    return numbers

def execute_game(numbers):
    dict_num_turns = dict()
    turn = 0    
    spoken_num = -1
    for num in numbers:
        turn += 1
        spoken_num = num
        dict_num_turns[num] = [-1, turn]
    
    if dict_num_turns.get(0) == None:
        turn += 1
        spoken_num = 0
        dict_num_turns[spoken_num] = [-1, turn]

    # 0,3,6|0
    while turn < 30000000:
        turn += 1
        if dict_num_turns[spoken_num][0] == -1:
            spoken_num = 0
            update_dict_value(dict_num_turns, spoken_num, turn)
        else:
            pair = dict_num_turns[spoken_num]
            spoken_num = pair[1] - pair[0] 
            if dict_num_turns.get(spoken_num) == None:  
                dict_num_turns[spoken_num] = [-1, turn]
            else:
                update_dict_value(dict_num_turns, spoken_num, turn)
    return spoken_num

def update_dict_value(dict_num_turns, key, new_value):
    pair = dict_num_turns[key]
    pair[0] = pair[1]
    pair[1] = new_value 
    dict_num_turns[key] = pair

numbers = read_input()
result = execute_game(numbers)
print(result)
