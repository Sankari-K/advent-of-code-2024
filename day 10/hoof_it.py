def get_puzzle_input(directory):
    with open(directory) as f:
        file = f.read().split()
    
    topographic_map = dict()
    for x, height_row in enumerate(file):
        for y, height in enumerate(height_row):
            topographic_map[(x, y)] = int(height)
    return topographic_map, len(file), len(file[0])

def get_hiking_trail_heads(topographic_map):
    return [coordinate for coordinate, item in topographic_map.items() if item == 0]

def get_score(x, y):
    if topographic_map[(x, y)] == 9:
        return {(x, y)}
    
    ans = set()
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in topographic_map and topographic_map[(new_x, new_y)] == topographic_map[(x, y)] + 1:
            ans.update(get_score(new_x, new_y))
    return ans

def get_rating(x, y):
    if topographic_map[(x, y)] == 9:
        return 1
    
    ans = 0
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in topographic_map and topographic_map[(new_x, new_y)] == topographic_map[(x, y)] + 1:
            ans += get_rating(new_x, new_y)
    return ans

def get_sum_scores():
    sum_scores = 0
    for trail_head in get_hiking_trail_heads(topographic_map):
        sum_scores += len(get_score(*trail_head))
    return sum_scores

def get_sum_ratings():
    sum_scores = 0
    for trail_head in get_hiking_trail_heads(topographic_map):
        sum_scores += get_rating(*trail_head)
    return sum_scores

topographic_map, X_LIMIT, Y_LIMIT = get_puzzle_input("./puzzle_input.txt")
print(get_sum_scores())
print(get_sum_ratings())