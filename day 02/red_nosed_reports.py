def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()

    return [list(map(int, line.strip().split())) for line in lines]

def check_increasing(report):
    for index, item in enumerate(report[1:], start=1):
        prev = report[index - 1]
        if item - prev not in [1, 2, 3]:
            return False
    return True

def check_increasing_with_dampener(report):
    return any([check_increasing(report[:index] + report[index + 1:]) for index in range(len(report))])

def find_safe_reports(reports, dampening=False):
    check = check_increasing_with_dampener if dampening else check_increasing 
    reports = list(map(lambda x: x if x[0] < x[-1] else x[::-1], reports))
    return sum(map(check, reports))

puzzle_input = get_puzzle_input(r"./puzzle_input.txt")

# part a
print(find_safe_reports(puzzle_input))

# part b
print(find_safe_reports(puzzle_input, True))