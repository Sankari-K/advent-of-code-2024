def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()
    
    return [list(map(int, line.strip().replace(":", "").split())) for line in lines]

def solve_eqn(current_result, operands, expected_result):
    if not operands:
        return current_result == expected_result
    if current_result > expected_result:
        return False
    return solve_eqn(current_result * operands[0], operands[1:], expected_result) \
        or solve_eqn(current_result + operands[0], operands[1:], expected_result)

def solve_modified_eqn(current_result, operands, expected_result):
    if not operands:
        return current_result == expected_result
    if current_result > expected_result:
        return False
    return solve_modified_eqn(current_result * operands[0], operands[1:], expected_result) \
        or solve_modified_eqn(current_result + operands[0], operands[1:], expected_result) \
        or solve_modified_eqn(int(f"{current_result}{operands[0]}"), operands[1:], expected_result)

def find_total_calibration(equations, solver_func):
    total_calibration = 0
    for res, *operands in equations:
        if solver_func(operands[0], operands[1:], res):
            total_calibration += res
    return total_calibration

equations = get_puzzle_input(r"./puzzle_input.txt")

import time
a = time.time()
print(find_total_calibration(equations, solve_eqn)) # part a
print(find_total_calibration(equations, solve_modified_eqn)) # part b
b = time.time()

print(b - a)

"""
Optimizations made:
1. Since the only operations are +, *, and ||, the value can only *increase* as we traverse through the operands.
   So if at any point, the current computed sum is greater than the result, we can break early. Brings down time from ~5s to ~3s.
2. Work backwards instead of forwards. This prunes a lot of the nodes, since we 1) won't go down the multiplication route if the last operand
   isn't a factor of the final result 2) won't go down the concat route if the digits of the last operand aren't the last digits of the result.
   This brings it down from ~3s to ~0.018s (!). Implementation in alternative.py <3
"""