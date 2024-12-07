def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()
    
    equations = []
    for line in lines:
        res, operands = line.strip().split(": ")
        operands = list(map(int, operands.split()))
        equations.append([operands, int(res)])
    return equations

def solve_eqn(current_result, operands, expected_result):
    if not operands:
        return current_result == expected_result
    
    return solve_eqn(current_result * operands[0], operands[1:], expected_result) \
        or solve_eqn(current_result + operands[0], operands[1:], expected_result)

def solve_modified_eqn(current_result, operands, expected_result):
    if not operands:
        return current_result == expected_result
    
    return solve_modified_eqn(current_result * operands[0], operands[1:], expected_result) \
        or solve_modified_eqn(current_result + operands[0], operands[1:], expected_result) \
        or solve_modified_eqn(int(str(current_result) + str(operands[0])), operands[1:], expected_result)

def find_total_calibration(equations, solver_func):
    total_calibration = 0
    for operands, res in equations:
        if solver_func(operands[0], operands[1:], res):
            total_calibration += res
    return total_calibration

equations = get_puzzle_input(r"./puzzle_input.txt")

print(find_total_calibration(equations, solve_eqn)) # part a
print(find_total_calibration(equations, solve_modified_eqn)) # part b