N = int(input())
tmp = []

for _ in range(N):
    S, T = input().split()
    tmp.append([int(T), S])

ans = sorted(tmp)

print(ans[-2][1])
