N = int(input())
ans = []

for i in range(N):
    S, P  = input().split()
    ans.append([S, -int(P), i + 1])

ans.sort()

for j in ans:
    print(j[2])