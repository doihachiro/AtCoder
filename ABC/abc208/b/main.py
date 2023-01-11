from math import factorial
P = int(input())
count = 0

for i in range(10, 0, -1):
    tmp = factorial(i)
    while tmp <= P:
        P -= tmp
        count += 1

print(count)