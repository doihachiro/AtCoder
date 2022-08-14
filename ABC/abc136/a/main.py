A, B, C = map(int, input().split())

X = C - (A - B)

if 0 <= X:
    print(X)
else:
    print(0)