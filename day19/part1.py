def test(s,seq): 
    if s == '' or seq == []:
        return s == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = rules[seq[0]]
    if '"' in r:
        if s[0] == r[1]:
            return test(s[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term
        

def parse_rules(text):
    rules = dict()
    for line in text:
        num, exp = line.split(': ')
        if '"' in exp:
            rules[int(num)] = exp
        else:   
            rules[int(num)] = [[int(y) for y in x.split()] for x in exp.split('|')]
    return rules

txt_rules, messages = [x.splitlines() for x in open('input.txt', 'r').read().split('\n\n')]
rules = parse_rules(txt_rules)
print('P1:', sum(test(m, [0]) for m in messages))

txt_rules += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = parse_rules(txt_rules)
print('P2:', sum(test(m, [0]) for m in messages))
