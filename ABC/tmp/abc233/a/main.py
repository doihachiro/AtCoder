import math
X, Y = map(int, input().split())

A = math.ceil((Y - X) / 10)

if 0 < A:
    print(A)
else:
    print(0)