from collections import defaultdict
from itertools import combinations

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split()
    
    roof = defaultdict(set)
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col != ".":
                roof[col].add((x, y))  
    return len(lines), len(lines[0]), roof

def find_antinode(a, b, newx):
    ax, ay = a
    bx, by = b
    slope = (by - ay) / (bx - ax)
    return (newx, slope * (newx - ax) + ay)

def check_bounds(antinode):
    return antinode[0] >= 0 and antinode[0] < X_LIMIT and antinode[1] >= 0 and antinode[1] < Y_LIMIT

def find_antinodes(frequency):
    antinodes = set()

    for (ax, ay), (bx, by) in combinations(roof[frequency], 2):
        x_diff = abs(ax - bx)
        
        for newx in [min(ax, bx) - x_diff, max(ax, bx) + x_diff]:
            newx, newy = find_antinode((ax, ay), (bx, by), newx)
            if check_bounds((newx, newy)):
                antinodes.add((newx, newy))

    return antinodes

def find_resonant_antinodes(frequency):
    antinodes = set()

    for a, b in combinations(roof[frequency], 2):
        for newx in range(0, X_LIMIT):
            newx, newy = find_antinode(a, b, newx)
            if newy >= 0 and newy < Y_LIMIT and newy == int(newy):
                antinodes.add((newx, newy))
    return antinodes

def find_all_antinodes(roof, consider_resonance=False):
    find_func = find_resonant_antinodes if consider_resonance else find_antinodes
    all_antinodes = set()

    for frequency in  roof.keys():
        all_antinodes.update(find_func(frequency))

    return len(all_antinodes)
 
X_LIMIT, Y_LIMIT, roof = get_puzzle_input(r"./puzzle_input.txt")
print(find_all_antinodes(roof)) # part a
print(find_all_antinodes(roof, True)) # part b

