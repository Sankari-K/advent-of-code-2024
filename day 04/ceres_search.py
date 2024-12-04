from collections import defaultdict

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.readlines()

    return [list(line.strip()) for line in lines]

def get_diagonal_word_search(word_search, operation):
    diagonal_word_search = defaultdict(list)
    for x in range(len(word_search)):
        for y in range(len(word_search[0])):
            diagonal_word_search[operation(x, y)].append(word_search[x][y])
    return list(diagonal_word_search.values())

def find_xmas(word_search):
    word_search = map(lambda x: "".join(x), word_search)
    return sum(line.count("XMAS") + line.count("SAMX") for line in word_search)

def find_all_xmas(word_search):
    word_searches = [
        word_search,
        list(map(list, zip(*word_search))),
        get_diagonal_word_search(word_search, lambda x, y: x + y),
        get_diagonal_word_search(word_search, lambda x, y: x - y)
    ]
    return sum(map(find_xmas, word_searches))

def find_all_x_mas(word_search):
    x_mas_amount = 0
    for x in range(1, len(word_search) - 1):
        for y in range(1, len(word_search[0]) - 1):
            if word_search[x][y] == "A" \
            and {word_search[x - 1][y - 1], word_search[x + 1][y + 1]} == {"M", "S"} \
            and {word_search[x + 1][y - 1], word_search[x - 1][y + 1]} == {"M", "S"}:
                x_mas_amount += 1
    return x_mas_amount
            
word_search = get_puzzle_input(r"./puzzle_input.txt")
print(find_all_xmas(word_search)) # part a
print(find_all_x_mas(word_search)) # part b