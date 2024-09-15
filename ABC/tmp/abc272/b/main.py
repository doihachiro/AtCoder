N, M = map(int, input().split())
P = [[0] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    kx = list(map(int, input().split()))
    k = kx[0]
    x = kx[1:]

    for i in range(k):
        for j in range(i+1, k):
            P[x[i]][x[j]] = 1

for l in range(1, N+1):
    for m in range(l+1, N+1):
        if P[l][m] == 0:
            print("No")
            exit()

print("Yes")