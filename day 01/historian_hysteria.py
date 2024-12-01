from collections import Counter

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()

    return [list(map(int, line.strip().split())) for line in lines]

def find_list_distance(input):
    left, right = map(sorted, zip(*input))
    return sum([abs(l - r) for l, r in zip(left, right)])

def find_similarity_score(input):
    left, right = zip(*input)
    right = Counter(right)
    return sum([l * right[l] for l in left])

# part a
puzzle_input = get_puzzle_input(r"./puzzle_input.txt")
print(find_list_distance(puzzle_input))

# part b
puzzle_input = get_puzzle_input(r"./puzzle_input.txt")
print(find_similarity_score(puzzle_input))