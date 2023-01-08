X, Y = map(int, input().split())

if Y % 2 != 0 or X * 4 < Y or Y < 2 * X:
    print("No")
else:
    print("Yes")