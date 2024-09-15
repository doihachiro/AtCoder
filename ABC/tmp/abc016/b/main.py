A, B, C = map(int, input().split())

X = A + B
Y = A - B

if C == X and C == Y:
    print("?")
elif C == X:
    print("+")
elif C == Y:
    print("-")
else:
    print("!")