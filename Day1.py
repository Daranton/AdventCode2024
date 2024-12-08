import os
print(os.getcwd())


with open('input.txt', 'r') as f:
        left = []
        right = []
        for line in f.readlines():
            pairs = line.split()
            left.append(pairs[0])
            right.append(pairs[1])
        sum = 0
        for i in range(len(left)):
            #print(left[i], right[i])
            difference = abs(int(left[i]) - int(right[i]))
            sum += difference
        print(sum)