N = int(input())
ans = 0

for i in range(N):
    x, y = input().split()
    if y == "BTC":
        x = float(x) * 380000.0
    ans += float(x)

print(ans)