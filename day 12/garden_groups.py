SEEN = set()
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split()

    GARDEN = dict()
    for x, row in enumerate(file):
        for y, col in enumerate(row):
            GARDEN[(x, y)] = col
    return len(file), len(file[0]), GARDEN

def get_details(x, y, cycle):
    if (x, y) in cycle or (x, y) in SEEN:
        return 0, 0, []
    if (x, y) not in GARDEN:
        return 0, 0, []
    
    perimeter = 0
    area = 1
    if x == 0 or x == X_LIMIT - 1:
        perimeter += 1
    if y == 0 or y == Y_LIMIT - 1:
        perimeter += 1

    points = [(x, y)]
    cycle.add((x, y))
    for dx, dy in DIRECTIONS:
        newx, newy = x + dx, y + dy
        if (newx, newy) in GARDEN and GARDEN[(x, y)] != GARDEN[(newx, newy)]:
            perimeter += 1
        else:
            extraarea, extraperimeter, extrapoints =  get_details(newx, newy, cycle)
            area += extraarea
            perimeter += extraperimeter
            points += extrapoints

    SEEN.add((x, y))
    cycle.remove((x, y))
    return area, perimeter, points
     
def get_fencing_price():
    price, discount_price = 0, 0
    for x in range(X_LIMIT):
        for y in range(Y_LIMIT):
            if (x, y) not in SEEN:
                area, perimeter, points = get_details(x, y, set())
                price += area * perimeter
                discount_price += area * get_sides(points)
                SEEN.add((x, y))
    return price, discount_price

def get_sides(region):
    up_sides = 0
    down_sides = 0
    left_sides = 0
    right_sides = 0

    for (x, y) in region:
        left = x - 1
        right = x + 1
        above = y - 1
        below = y + 1
        right_not_in_region = (right, y) not in region
        below_not_in_region = (x, below) not in region

        if (x, above) not in region:
            if right_not_in_region or (right, above) in region:
                up_sides += 1

        if (x, below) not in region:
            if right_not_in_region or (right, below) in region:
                down_sides += 1

        if (left, y) not in region:
            if below_not_in_region or (left, below) in region:
                left_sides += 1

        if (right, y) not in region:
            if below_not_in_region or (right, below) in region:
                right_sides += 1

    return up_sides + down_sides + left_sides + right_sides

X_LIMIT, Y_LIMIT, GARDEN = get_puzzle_input("./puzzle_input.txt")
print(get_fencing_price())
