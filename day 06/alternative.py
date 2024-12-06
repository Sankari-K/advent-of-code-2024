def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read().split()
    
    obstacles = set()
    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if col == "#":
                obstacles.add(complex(x, y))
            if col == "^":
                current = complex(x, y)
    return len(lines), len(lines[0]), current, obstacles

def traverse_map(current_position, obstacles):
    seen = set()
    current_dir = -1
    
    while current_position.real not in [-1, X_LIMIT] and current_position.imag not in [-1, Y_LIMIT]:
        seen.add(current_position)
        next_position = current_position + current_dir
        while next_position in obstacles:
            current_dir *= -1j
            next_position = current_position + current_dir

        current_position = next_position

    return seen

def find_loop(X_LIMIT, Y_LIMIT, current_position, obstacles):
    seen = set()
    current_dir = -1

    while current_position.real not in [-1, X_LIMIT] and current_position.imag not in [-1, Y_LIMIT]:
        next_position = current_position + current_dir
        while next_position in obstacles:
            current_dir *= -1j
            next_position = current_position + current_dir

        current_position = next_position
        if (current_dir, current_position) in seen:
            return True
        
        seen.add((current_dir, current_position))

    return False

def check_traversed_map(start_position, obstacles, seen):
    obstacle_positions = 0
    for seen_pos in seen:
        if seen_pos not in obstacles and seen_pos != start_position:
            if find_loop(X_LIMIT, Y_LIMIT, start_position, obstacles | {seen_pos}):
                obstacle_positions += 1
    return obstacle_positions

X_LIMIT, Y_LIMIT, start, obstacles = get_puzzle_input(r"./puzzle_input.txt")

seen = traverse_map(start, obstacles) # part a
print(len(seen))

print(check_traversed_map(start, obstacles, seen)) # part b
