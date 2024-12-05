from collections import defaultdict

def get_puzzle_input(directory):
    with open(directory) as f:
        lines = f.read()

    return map(lambda x: x.split(), lines.split("\n\n"))

def transform_rules(page_ordering_rules):
    rules = defaultdict(set) # x|y => x must be before y   rules[y(next)] = {x(prev),}
    for rule in page_ordering_rules:
        prev, next = map(int, rule.split("|"))
        rules[next].add(prev)
    return rules

def transform_updates(updates):
    return [list(map(int, update.split(","))) for update in updates] 

def check_ordering(rules, update): # check if update is correctly ordered or not
    for index, next in enumerate(update):
        for potential_prev in rules[next]:
            if potential_prev in update and update.index(potential_prev) > index:
                return False
    return True

def reorder_update(rules, update):
    while not check_ordering(rules, update):
        for next in update:
            for element in rules[next].intersection(update[update.index(next) + 1:]):
                update.remove(element)
                update.insert(update.index(next), element)
    return update

def get_updates_subset(rules, updates):
    return filter(lambda x: check_ordering(rules, x), updates)

def get_reorder_updates_subset(rules, updates):
    updates = filter(lambda x: not check_ordering(rules, x), updates)
    return list(map(lambda x: reorder_update(rules, x), updates))

def sum_page_numbers(updates):
    return sum(map(lambda x: x[len(x) // 2], updates))

page_ordering_rules, updates = get_puzzle_input(r"./puzzle_input.txt")
rules = transform_rules(page_ordering_rules)
updates = transform_updates(updates)

# part a
print(sum_page_numbers(get_updates_subset(rules, updates)))

# part b
print(sum_page_numbers(get_reorder_updates_subset(rules, updates)))