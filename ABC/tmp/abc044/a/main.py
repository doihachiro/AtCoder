N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N < K:
    print(X * N)
else:
    print(K * X + (N - K) * Y)