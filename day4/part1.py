def process_data(data, req_fields):
    valid_passports = 0
    for line in data.split('\n'):
        if line == '':
            if all(req_fields.values()):
                valid_passports += 1
            req_fields = dict.fromkeys(req_fields, False)
        else:
            for field in line.split(' '):
                key = field.split(':')[0]
                if req_fields.get(key) == False:
                    req_fields[key] = True
    return valid_passports

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
        
    rd.close()
    return text

required_fields = {
        'byr': False,
        'iyr':False,
        'eyr':False,
        'hgt':False,
        'hcl':False,
        'ecl':False,
        'pid':False
        }

text = read_file()
result = process_data(text, required_fields)
print(result)
