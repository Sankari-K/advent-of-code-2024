DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split()
    
    obstacles = set()
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col == "#":
                obstacles.add((x, y))
            if col == "^":
                current = (x, y)
    return len(lines), len(lines[0]), current, obstacles

def traverse_map(current_position, obstacles):
    seen = set()
    current_dir = 0

    while (current_position[0] not in [-1, X_LIMIT]) and (current_position[1] not in [-1, Y_LIMIT]):
        seen.add(current_position)
        next_position = (current_position[0] + DIRECTIONS[current_dir][0]), (current_position[1] + DIRECTIONS[current_dir][1])
        while next_position in obstacles:
            current_dir = (current_dir + 1) % len(DIRECTIONS)
            next_position = (current_position[0] + DIRECTIONS[current_dir][0]), (current_position[1] + DIRECTIONS[current_dir][1])

        current_position = next_position

    return seen

def find_loop(X_LIMIT, Y_LIMIT, current_position, obstacles):
    seen = set()
    current_dir = 0

    while current_position[0] not in [-1, X_LIMIT] and current_position[1] not in [-1, Y_LIMIT]:
        next_position = (current_position[0] + DIRECTIONS[current_dir][0]), (current_position[1] + DIRECTIONS[current_dir][1])
        while next_position in obstacles:
            current_dir = (current_dir + 1) % len(DIRECTIONS)
            next_position = (current_position[0] + DIRECTIONS[current_dir][0]), (current_position[1] + DIRECTIONS[current_dir][1])

        current_position = next_position
        if (current_dir, current_position) in seen:
            return True
        
        seen.add((current_dir, current_position))

    return False

def check_traversed_map(start_position, obstacles, seen):
    obstacle_positions = 0
    for x, y in seen:
        if (x, y) not in obstacles and (x, y) != start_position:
            if find_loop(X_LIMIT, Y_LIMIT, start_position, obstacles | {(x, y)}):
                obstacle_positions += 1
    return obstacle_positions

X_LIMIT, Y_LIMIT, start, obstacles = get_puzzle_input(r"./puzzle_input.txt")

seen = traverse_map(start, obstacles) # part a
print(len(seen))

print(check_traversed_map(start, obstacles, seen)) # part b