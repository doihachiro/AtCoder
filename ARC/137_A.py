import math

L, R = map(int, input().split())

for x in reversed(range(R)):
    if math.gcd(L, x) == 1:
        R = x
        break
    else:
        x += 1

print(R - L)