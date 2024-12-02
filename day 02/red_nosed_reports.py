def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()

    return [list(map(int, line.strip().split())) for line in lines]

def check_increasing(report):
    return all(map(lambda x: x[1] - x[0] in [1, 2, 3], zip(report, report[1:]))) # x = (prev_level, level)

def check_increasing_with_dampener(report):
    return any([check_increasing(report[:index] + report[index + 1:]) for index in range(len(report))])

def find_safe_reports(reports, dampening=False):
    check = check_increasing_with_dampener if dampening else check_increasing 
    return sum(map(lambda x: check(x) or check(x[::-1]), reports))

puzzle_input = get_puzzle_input(r"./puzzle_input.txt")

# part a
print(find_safe_reports(puzzle_input))

# part b
print(find_safe_reports(puzzle_input, True))