import re

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()
    return lines

def get_enabled_memory(memory):
    enabled_memory = []
    for match in re.split(r"do\(\)", "".join(memory)):
        index = match.find("don't()")
        index = index if index != -1 else len(match)
        enabled_memory.append(match[:index])
    return enabled_memory

def find_multiplication_result(memory):
    result = 0
    pattern = r'mul\((\d*),(\d*)\)'
    for line in memory:
        for match in re.findall(pattern, line):
            result += int(match[0]) * int(match[1])
    return result

memory = get_puzzle_input(r"./puzzle_input.txt")
print(find_multiplication_result(memory)) # part a
print(find_multiplication_result(get_enabled_memory(memory))) # part b