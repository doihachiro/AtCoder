N, M, X= map(int, input().split())
A = list(map(int, input().split()))

A.append(X)
A.sort()

print(min(A.index(X), M - A.index(X)))