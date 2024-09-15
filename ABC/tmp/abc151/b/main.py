N, K, M = map(int, input().split())
A = list(map(int, input().split()))
X = N * M

if K < (X - sum(A)):
    print(-1)
elif X < sum(A):
    print(0)
else:
    print(X - sum(A))