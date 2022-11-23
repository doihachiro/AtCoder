N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
count = 0

for _ in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j] * B[j]
    if 0 < ans + C:
        count += 1

print(count)