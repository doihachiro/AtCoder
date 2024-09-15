X, Y, Z = map(int, input().split())

if (0 < Y < Z and Y < X) or (Z < Y < 0 and X < Y):
    print(-1)
    exit()
elif 0 < X < Y or Y < 0 < X:
    print(X)
    exit()
elif Y < X < 0 or X < 0 < Y :
    print(abs(X))
    exit()
else:
    print(abs(Z) + abs(X - Z))
    exit()