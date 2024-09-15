N = int(input())
tmp = [[] for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        if j == 0 or i == j:
            tmp[i].append(1)
        else:
            tmp[i].append(tmp[i-1][j-1] + tmp[i-1][j])

for k in tmp:
    print(*k)