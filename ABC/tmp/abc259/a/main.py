N, M, X, T, D = map(int, input().split())
A = X - M

if X <= M:
    print(T)
else:
    print(T - A * D)