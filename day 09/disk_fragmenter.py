def get_puzzle_input(directory):
    with open(directory) as f:
        return list(map(int, f.read().strip()))

def get_individual_representation(disk_map):
    individual_representation = []
    for index, item in enumerate(disk_map):
        if index % 2 == 0: # length of file
            individual_representation += [index // 2] * item
        else: # free space
            individual_representation += ["."] * item
    return individual_representation

def move_file_blocks(disk_map):
    rightmost_index = len(disk_map) - 1

    while disk_map[rightmost_index] == ".":
        rightmost_index -= 1

    for index, item in enumerate(disk_map[:len(disk_map) - disk_map.count(".")]):
        if item == ".":
            disk_map[index], disk_map[rightmost_index] = disk_map[rightmost_index], disk_map[index]

            while disk_map[rightmost_index] == ".":
                rightmost_index -= 1    
    return disk_map

def modified_move_file_blocks(disk_map):
    rightmost_index = len(disk_map) - 1
    while disk_map[rightmost_index] == ".":
        rightmost_index -= 1
    
    while rightmost_index >= 0:
        file_space = disk_map.count(disk_map[rightmost_index])
        free_count = 0
        for index, item in enumerate(disk_map[:rightmost_index]):
            if item == ".":
                free_count += 1
                if free_count == file_space:
                    disk_map[index - free_count + 1:index + 1], disk_map[rightmost_index - free_count + 1:rightmost_index + 1] = \
                    disk_map[rightmost_index - free_count + 1:rightmost_index + 1], disk_map[index - free_count + 1:index + 1]
                    break
            else:
                free_count = 0

        rightmost_index = rightmost_index - file_space
        while disk_map[rightmost_index] == ".":
            rightmost_index -= 1
    return disk_map
            
def get_checksum(disk_map):
    checksum = 0
    for index, item in enumerate(disk_map): 
        if item == ".":
            continue
        checksum += index * int(item)
    return checksum

disk_map = get_individual_representation(get_puzzle_input("./puzzle_input.txt"))

disk_map = move_file_blocks(disk_map) # part a
print(get_checksum(disk_map)) 

disk_map = modified_move_file_blocks(disk_map) # part b
print(get_checksum(disk_map)) 

