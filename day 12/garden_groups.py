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
        return 0, 0
    if (x, y) not in GARDEN:
        return 0, 0
    
    perimeter = 0
    area = 1
    if x == 0 or x == X_LIMIT - 1:
        perimeter += 1
    if y == 0 or y == Y_LIMIT - 1:
        perimeter += 1

    cycle.add((x, y))
    for dx, dy in DIRECTIONS:
        newx, newy = x + dx, y + dy
        if (newx, newy) in GARDEN and GARDEN[(x, y)] != GARDEN[(newx, newy)]:
            perimeter += 1
        else:
            extraarea, extraperimeter =  get_details(newx, newy, cycle)
            area += extraarea
            perimeter += extraperimeter
    SEEN.add((x, y))
    cycle.remove((x, y))
    return area, perimeter
    
    
def get_fencing_price():
    price = 0
    for x in range(X_LIMIT):
        for y in range(Y_LIMIT):
            if (x, y) not in SEEN:
                area, perimeter = get_details(x, y, set())
                price += area * perimeter
                SEEN.add((x, y))
    return price

X_LIMIT, Y_LIMIT, GARDEN = get_puzzle_input("./puzzle_input.txt")
print(get_fencing_price())