A, B = map(int, input().split())
C = A + B

if 15 <= C and 8 <= B:
    print(1)
elif 10 <= C and 3 <= B:
    print(2)
elif 3 <= C:
    print(3)
else:
    print(4)