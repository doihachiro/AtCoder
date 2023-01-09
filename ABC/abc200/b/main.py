N, K = map(int, input().split())
ans = N

for i in range(K):
    if ans % 200 == 0:
        ans //= 200
    else:
        ans = int(str(ans) + "200")

print(ans)