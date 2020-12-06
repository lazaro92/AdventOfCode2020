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
                value = field.split(':')[1]
                if req_fields.get(key) == False and conditions[key](value):
                    req_fields[key] = True
    return valid_passports

def read_file():
    rd = open('input.txt', 'r')
    text = rd.read()
        
    rd.close()
    return text

required_fields = {
        'byr': False,
        'iyr': False,
        'eyr': False,
        'hgt': False,
        'hcl': False,
        'ecl': False,
        'pid': False
        }

conditions = {
        'byr': lambda x: 1920 <= int(x) and int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) and int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) and int(x) <= 2030,

        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) and int(x[:-2]) <= 193) or
        (x[-2:] == 'in' and 59 <= int(x[:-2]) and int(x[:-2]) <= 76),
        
        'hcl': lambda x: len(x) == 7 and x[0] == '#' and
        all(map(lambda y: (48 <= ord(y) and ord(y) <= 57) or
            (97 <= ord(y) and ord(y) <= 102), list(x)[1:])),

        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: len(x) == 9 and x.isdigit()
        }

text = read_file()
result = process_data(text, required_fields)
print result
