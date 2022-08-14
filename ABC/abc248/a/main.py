S = list(map(int, input()))
N = list(range(10))

A = list(set(S) ^ set(N))
print(A[0])