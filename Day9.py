with open('./Day9input.txt') as f:
    # input_line = f.read().strip()
    #print(input_line)
    line = f.read().strip()
    # for i, ch in enumerate(line): # Used later in code
    #     print(i, int(ch))

def odd_even(diskmap): # odd = file, even = free space (no variable, spews as byproduct in "else"), diskmap = input value
    blocks = []

    odd = True
    id = 0
    for number in diskmap:
        number = int(number)
        if odd:
            blocks += [id] * number
            id += 1
            odd = False
            #print("File_Block")
            #return True
        else:
            blocks += [None] * number
            odd = True
            #print("Free_Space")
            #return False
        #print(number) # Spews single integers from input value
    #print(diskmap) # Spews whole input value
    return blocks

filesystem = odd_even(line)

def move(array): #For part 1
    first_free = 0
    while array[first_free] != None:
        first_free += 1

    i = len(array) - 1
    while array[i] == None:
        i -= 1

    while i > first_free:
        array[first_free] = array[i]
        array[i] = None
        while array[i] == None:
            i -= 1
        while array[first_free] != None:
            first_free += 1

    return array

def checksum(array):
        output = 0
        for id, number in enumerate(array):
            if number != None:
                output += id * number
        return output


output = checksum(move(filesystem))
print(output)
#print(line) # Spews input value