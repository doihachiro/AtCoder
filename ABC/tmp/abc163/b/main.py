N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = N - sum(A)

if 0 <= ans:
    print(ans)
else:
    print(-1)