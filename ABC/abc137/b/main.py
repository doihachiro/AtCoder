K, X = map(int, input().split())
ans = []

for i in range(K * 2 - 1):
    ans.append(X - K + i + 1)

print(*ans)