X, K = map(int, input().split())

for i in range(K):
    P = 10 ** (i + 1)
    A = (X % P) // (P // 10)
    B = X // P
    if A >= 5:
        X = (B + 1) * P
    else:
        X = B * P

print(X)