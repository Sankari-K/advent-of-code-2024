DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def get_puzzle_input(directory):
    with open(directory) as f:
        file = f.read().split()
    
    TOPOGRAPHIC_MAP = dict()
    for x, height_row in enumerate(file):
        for y, height in enumerate(height_row):
            TOPOGRAPHIC_MAP[(x, y)] = int(height)
    return TOPOGRAPHIC_MAP, len(file), len(file[0])

def get_hiking_trail_heads(TOPOGRAPHIC_MAP):
    return [coordinate for coordinate, item in TOPOGRAPHIC_MAP.items() if item == 0]

def get_score(x, y):
    if TOPOGRAPHIC_MAP[(x, y)] == 9:
        return {(x, y)}
    
    ans = set()
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in TOPOGRAPHIC_MAP and TOPOGRAPHIC_MAP[(new_x, new_y)] == TOPOGRAPHIC_MAP[(x, y)] + 1:
            ans.update(get_score(new_x, new_y))
    return ans

def get_rating(x, y):
    if TOPOGRAPHIC_MAP[(x, y)] == 9:
        return 1
    
    ans = 0
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in TOPOGRAPHIC_MAP and TOPOGRAPHIC_MAP[(new_x, new_y)] == TOPOGRAPHIC_MAP[(x, y)] + 1:
            ans += get_rating(new_x, new_y)
    return ans

def get_sum_scores():
    return sum(map(lambda x: len(get_score(*x)), get_hiking_trail_heads(TOPOGRAPHIC_MAP)))

def get_sum_ratings():
    return sum(map(lambda x: get_rating(*x), get_hiking_trail_heads(TOPOGRAPHIC_MAP)))

TOPOGRAPHIC_MAP, X_LIMIT, Y_LIMIT = get_puzzle_input("./puzzle_input.txt")
print(get_sum_scores())
print(get_sum_ratings())