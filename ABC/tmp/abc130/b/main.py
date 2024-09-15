N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = [0]
count = 0

for i in range(1, N+1):
    ans.append(ans[i-1] + L[i-1])

for j in ans:
    if j <= X:
        count += 1

print(count)