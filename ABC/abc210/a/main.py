N, A, X, Y= map(int, input().split())

B = N - A

if N > A:
    print(X * A + Y * B)
else:
    print(N * X)