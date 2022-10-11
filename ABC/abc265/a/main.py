X, Y, N = map(int, input().split())

if X * 3 > Y:
    A = N // 3
    B = N % 3
    print((Y * A) + (X * B))
else:
    print(X * N)