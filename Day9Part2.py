from tqdm import tqdm

with open('./Day9input.txt') as f:
    line = f.read().strip()

size = [0] * len(line)
loc = [0] * len(line)


def odd_even(diskmap): # odd = file, even = free space (no variable, spews as byproduct in "else"), diskmap = input value
    global loc, size

    blocks = []

    odd = True
    id = 0
    for number in diskmap:
        number = int(number)
        if odd:
            loc[id] = len(blocks)
            size[id] = number
            blocks += [id] * number
            id += 1
            odd = False
        else:
            blocks += [None] * number
            odd = True

    return blocks

filesystem = odd_even(line)

def move(array):

    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for to_move in tqdm(range(big, -1, -1)):
        # Finding working free space
        free_space = 0
        first_free = 0
        while first_free < loc[to_move] and free_space < size[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while array[first_free] != None:
                first_free += 1
            while first_free + free_space < len(array) and array[first_free + free_space] == None:
                free_space += 1

        if first_free >= loc[to_move]:
            continue

        for idx in range(first_free, first_free + size[to_move]):
            array[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + size[to_move]):
            array[idx] = None

    return array

def checksum(array):
        output = 0
        for id, number in enumerate(array):
            if number != None:
                output += id * number
        return output


# output = checksum(move(filesystem))
# print(output)

moved = move(filesystem)
print(checksum(moved))
#print(line) # Spews input value