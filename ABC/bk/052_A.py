A, B, C, D = map(int, input().split())
AB = A * B
CD = C * D

if AB > CD:
    print(AB)
elif AB < CD:
    print(CD)
else:
    print(AB)