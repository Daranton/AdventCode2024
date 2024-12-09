from numpy import loadtxt, sort
from collections import defaultdict

A, B = sort(loadtxt('/home/incorporated/Documents/IT/Python/AdventCode2024/Day1input.txt').T)
print(sum(abs(A - B)))

sum = 0
similiarity_score = defaultdict(int)
for x in B:
    similiarity_score[x] += 1
for x in A:
    sum += x * similiarity_score[x]

print(sum)