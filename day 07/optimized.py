def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()
    
    return [list(map(int, line.strip().replace(":", "").split())) for line in lines]

def solve_eqn(expected_result, operands):
    if len(operands) == 1:
        return expected_result == operands[0]
    
    return (expected_result % operands[-1] == 0 and solve_eqn(expected_result // operands[-1], operands[:-1])) \
    or solve_eqn(expected_result - operands[-1], operands[:-1])

def solve_modified_eqn(expected_result, operands):
    if len(operands) == 1:
        return expected_result == operands[0]
    
    return (expected_result % operands[-1] == 0 and solve_modified_eqn(expected_result // operands[-1], operands[:-1])) \
    or solve_modified_eqn(expected_result - operands[-1], operands[:-1]) \
    or (str(expected_result).endswith(str(operands[-1])) and solve_modified_eqn(expected_result // 10 ** len(str(operands[-1])), operands[:-1]))

def find_total_calibration(equations, solver_func):
    total_calibration = 0
    for res, *operands in equations:
        if solver_func(res, operands):
            total_calibration += res
    return total_calibration

equations = get_puzzle_input(r"./puzzle_input.txt")

print(find_total_calibration(equations, solve_eqn)) # part a
print(find_total_calibration(equations, solve_modified_eqn)) # part b