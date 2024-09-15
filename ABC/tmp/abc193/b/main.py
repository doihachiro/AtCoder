N = int(input())
ans = []

for _ in range(N):
    # A: minute, P: price, X: number
    A, P, X = map(int, input().split())
    if A + 0.5 < X:
        ans.append(P)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))