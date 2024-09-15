N, M = map(int, input().split())

for i in range(N+1):
    j = 4*N - M - 2*i
    k = M + i - 3*N
    if 0 <= j and 0 <= k:
        print(i, j, k)
        exit()

print(-1, -1, -1)