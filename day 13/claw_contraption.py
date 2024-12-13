def get_puzzle_input(directory):
    with open(directory) as file:
        file = file.read().split("\n\n")
        MACHINES = []
        for machine in file:
            a, b, p = machine.split("\n")
            ax, ay = a[a.index(":") + 1:].split(",")
            bx, by = b[b.index(":") + 1:].split(",")
            px, py = p[p.index(":") + 1:].split(",")
            ax, ay = int(ax[ax.index("+") + 1:]), int(ay[ay.index("+") + 1:])
            bx, by = int(bx[bx.index("+") + 1:]), int(by[by.index("+") + 1:])
            px, py = int(px[px.index("=") + 1:]), int(py[py.index("=") + 1:])

            MACHINES.append([ax, ay, bx, by, px, py])
    return MACHINES

def eqn_solver(ax, bx, px, ay, by, py, max_presses):
    if (px * by - bx * py) % (ax * by - ay * bx) != 0:
        return 0
    x = (px * by - bx * py) // (ax * by - ay * bx)

    if (py - (ay * x)) % by != 0:
        return 0
    y = (py - (ay * x)) // by

    if x < 0 or x > max_presses or y < 0 or y > max_presses:
        return 0
    return 3 * x + y
  
def find_fewest_tokens(MACHINES, error_found=False):
    tokens = 0
    max_presses = 100
    for machine in MACHINES:
        ax, ay, bx, by, px, py = machine
        if error_found:
            px += 10000000000000
            py += 10000000000000
            max_presses = float("inf")

        tokens += eqn_solver(ax, bx, px, ay, by, py, max_presses)
    return tokens

MACHINES = get_puzzle_input("./puzzle_input.txt")
print(find_fewest_tokens(MACHINES))
print(find_fewest_tokens(MACHINES, True))


