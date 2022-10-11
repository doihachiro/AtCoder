N = int(input())
A = list(map(int, input().split()))
X = 0

for i in range(N):
    X += A[i]

print(X)