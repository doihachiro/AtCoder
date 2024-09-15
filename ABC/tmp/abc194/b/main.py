N = int(input())
ans = 10 ** 6
A = []
B = []


for _ in range(N):
    X, Y = map(int, input().split())
    A.append(X)
    B.append(Y)

for i in range(N):
    for j in range(N):
        if i == j:
            tmp = A[i] + B[j]
        else:
            tmp = max(A[i], B[j])
        ans = min(ans, tmp)

print(ans)