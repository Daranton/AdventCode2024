from re import findall

fin = open('./Day3input.txt')
total1 = 0
total2 = 0

# Part 1:
# Separate regex patterns by ","
# for a, b in findall(r"mul\((\d+),(\d+)\)", fin.read()):
# 	total += int(a) * int(b) # Multiply

# print('Part 1:', total)

# Part 2:
enabled = True

# Separate regex patterns by ","
# Logical OR operator " | "

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", fin.read()):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b) # Multiply

        total1 += x
        total2 += x * enabled

print('Part 1:', total1)
print('Part 2:', total2)