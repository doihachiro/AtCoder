N, M = map(int, input().split())
S = [input() for _ in range(N)]
count = 0

for i in range(N):
    for j in range(i+1, N):
        OK = True
        for k in range(M):
            if (S[i][k] == "x" and S[j][k] == "x"):
                OK = False
        if OK:
            count += 1

print(count)