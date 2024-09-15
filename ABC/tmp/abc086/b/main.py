import math
a, b = input().split()
x = math.sqrt(int(a + b))

if x.is_integer():
    print("Yes")
else:
    print("No")
