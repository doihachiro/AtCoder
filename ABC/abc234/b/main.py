N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for x1, y1 in xy:
    for x2, y2 in xy:
        ans = max(ans, (x2 - x1) ** 2 + (y2 - y1) ** 2)

print(ans ** 0.5)