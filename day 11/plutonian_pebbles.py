from collections import defaultdict

def get_puzzle_input(directory):
    with open(directory) as file:
        return list(map(int, file.read().split()))

def simulate_one_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.extend([int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])])
        else:
            new_stones.append(stone * 2024)
    return new_stones

def simulate_blinks(stones, amount):
    for _ in range(amount):
        stones = simulate_one_blink(stones)
    return len(stones)

def optimized_simulate_blinks(stones, amount):
    stones_map =  defaultdict(int)
    for stone in stones:
        stones_map[stone] += 1
    
    new_stones_map = defaultdict(int)
    for _ in range(amount):
        for stone, freq in stones_map.items():
            if stone == 0:
                new_stones_map[1] += freq
            elif len(str(stone)) % 2 == 0:
                new_stones_map[int(str(stone)[:len(str(stone)) // 2])] += freq
                new_stones_map[int(str(stone)[len(str(stone)) // 2:])] += freq
            else:
                new_stones_map[stone * 2024] += freq
        stones_map, new_stones_map = new_stones_map, defaultdict(int)

    return sum(list(stones_map.values()))
            
stones = get_puzzle_input("./puzzle_input.txt")
print(simulate_blinks(stones, 25))
print(optimized_simulate_blinks(stones, 75))

