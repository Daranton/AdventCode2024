from numpy import loadtxt, sort

A, B = sort(loadtxt('/home/incorporated/Documents/IT/Python/AdventCode2024/input.txt').T)
print(sum(abs(A - B)))
