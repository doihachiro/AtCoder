N = int(input())
S = []

for _ in range(N):
    S.append(input())

for i in range(N):
    ans = ""
    for j in reversed(range(N)):
        ans += S[j][i]
    print(ans)