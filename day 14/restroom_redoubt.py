from collections import defaultdict
from functools import reduce
import sys

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().splitlines()

    robots = []
    for line in file:
        position, velocity = line.split()
        position = list(map(int, position[position.index("=") + 1:].split(",")))
        velocity = list(map(int, velocity[velocity.index("=") + 1:].split(",")))
        robots.append([position, velocity])
    return robots

def simulate(seconds):
    bathroom = defaultdict(int)
    for robot in ROBOTS:
        (px, py), (vx, vy) = robot 
        for _ in range(seconds):
            px = (px + vx) % X_LIMIT
            py = (py + vy) % Y_LIMIT
        bathroom[(px, py)] += 1
    return bathroom

def get_safety_factor(bathroom):
    quadrants = defaultdict(int)
    for x, y in bathroom.keys():
        if x != X_LIMIT // 2 and y != Y_LIMIT // 2:
            quadrants[(x < X_LIMIT // 2, y < Y_LIMIT // 2)] += bathroom[(x, y)]
    return reduce(lambda x, y: x * y, quadrants.values(), 1)

def check_arrangement():
    bathroom = defaultdict(int)
    for robot in ROBOTS:
        (px, py), (vx, vy) = robot 
        bathroom[(px, py)] += 1

    seconds = 1
    while True:
        for index, robot in enumerate(ROBOTS):
            (px, py), (vx, vy) = robot 
            bathroom[(px, py)] -= 1
            if bathroom[(px, py)] == 0:
                del bathroom[(px, py)]
            px = (px + vx) % X_LIMIT
            py = (py + vy) % Y_LIMIT
            ROBOTS[index] = [(px, py), (vx, vy)]
            bathroom[(px, py)] += 1
            
        if len(bathroom) == 500:
            return seconds
        seconds += 1

ROBOTS = get_puzzle_input("./puzzle_input.txt")
X_LIMIT, Y_LIMIT = 101, 103 # example: 11, 7 actual: 101, 103

# part 1
bathroom = simulate(100)
print(get_safety_factor(bathroom))

# part 2
print(check_arrangement())
