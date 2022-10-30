A = int(input())
B = int(input())

X = abs(B - A)
Y = 10 - A + B
Z = 10 + A - B

if A > B:
    if X < Y:
        print(X)
    else:
        print(Y)
else:
    if X < Z:
        print(X)
    else:
        print(Z)