N, A, B = map(int, input().split())
ans = []

for i in range(1, N+1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    if A <= tmp and tmp <= B:
        ans.append(i)

print(sum(ans))