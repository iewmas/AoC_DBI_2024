import re

def mul(a, b):
    return a * b


def scan_memory(mem):
    result = 0
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", mem)

    for m in matches:
        result = result + eval(m)

    return result


def scan_memory_conditional(mem):
    result = 0
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", mem)
    FLAG_ENABLED = True 

    for m in matches:
        if m.startswith('don'): FLAG_ENABLED = False
        elif m.startswith('do'): FLAG_ENABLED = True
        else:
            if FLAG_ENABLED: result = result + eval(m)

    return result