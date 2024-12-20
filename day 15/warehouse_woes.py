from collections import defaultdict

DIRECTIONS = {"<": -1j, ">": 1j, "^": -1, "v": 1}

def get_puzzle_input(directory):
    with open(directory) as f:
        warehouse_grid, movements = f.read().split("\n\n")
        warehouse_grid = warehouse_grid.split("\n")
    
    warehouse = defaultdict(str)
    for x, row in enumerate(warehouse_grid):
        for y, col in enumerate(row):
            warehouse[complex(x, y)] = col
    return warehouse, movements.replace("\n", ""), len(warehouse_grid), len(warehouse_grid[0])

def get_current():
   for coordinates, item in WAREHOUSE.items():
       if item == "@":
           return coordinates

def make_space(object, coordinate, direction):
    # make space in the "coordinate" coordinate for "object"
    if WAREHOUSE[coordinate] == "#":
        return False
    elif WAREHOUSE[coordinate] == "." or \
        make_space(WAREHOUSE[coordinate], coordinate + direction, direction):
        WAREHOUSE[coordinate] = object
        WAREHOUSE[coordinate - direction] = "."
        return True
    return False

def simulate_movements():
    for movement in MOVEMENTS:
        next = get_current() + DIRECTIONS[movement]
        make_space("@", next, DIRECTIONS[movement])

def get_gps_sum():
    gps_sum = 0
    for coordinate, item in WAREHOUSE.items():
        if item == "O":
            gps_sum += 100 * coordinate.real + coordinate.imag
    return gps_sum

# def display():
#     for x in range(X):
#         for y in range(Y):
#             print(WAREHOUSE[complex(x, y)], end="")
#         print()

WAREHOUSE, MOVEMENTS, X, Y = get_puzzle_input("./puzzle_input.txt")

# part a
simulate_movements()
print(int(get_gps_sum()))



