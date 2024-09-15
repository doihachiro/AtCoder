N, M = map(int, input().split())
tmp = [[False] * N for _ in range(N+1)]
ans = 0

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    tmp[U][V] = True
    tmp[V][U] = True

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if tmp[i][j] and tmp[j][k] and tmp[k][i]:
                ans += 1

print(ans)