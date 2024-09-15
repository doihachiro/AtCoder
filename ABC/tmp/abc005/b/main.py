N = int(input())
A = 100

for i in range(N):
    X = int(input())
    A = min(A, X)

print(A)