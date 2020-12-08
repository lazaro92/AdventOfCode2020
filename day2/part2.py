def process_data(data):
    num_valid_password = 0
    for element in data:
        found = False
        for pos in element[0]:
            if element[2][pos-1] == element[1]:
                num_valid_password += 1
                if found:
                    num_valid_password -= 2
                found = True
    return num_valid_password

def read_file():
    data = []
    rd = open('input.txt', 'r')
    while True:
        line = rd.readline()
        if not line:
            break;
        data.append(extract_line_info(line))
    rd.close()
    return data

def extract_line_info(line):
    splited = line.split(' ')
    range_char = splited[0].split('-')
    return [int(range_char[0]), int(range_char[1])], splited[1][0], splited[2]

data = read_file()
results = process_data(data)
print ('number of valid passwords: ', results)
