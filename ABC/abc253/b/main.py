H, W = map(int, input().split())
S = []
ans = []

for _ in range(H):
    S.append(input())

for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            ans.append([i, j])

print(abs(ans[0][0] - ans[1][0]) + abs(ans[0][1] - ans[1][1]))