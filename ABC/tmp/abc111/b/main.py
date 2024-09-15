N = int(input())

if N % 111 == 0:
    print(N)
else:
    X = str(N // 111 + 1)
    print(3 * X)