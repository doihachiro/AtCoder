N, K = map(int, input().split())
R = list(map(int, input().split()))
ans = 0

R.sort()
for i in range(N-K, N):
    ans = (ans + R[i]) / 2

print(ans)