N = int(input())
tmp = []

for _ in range(N):
    tmp.append(list(map(int, input().split())))

for i in range(N):
    tmp[i] = tuple(tmp[i])

ans = tuple(tmp)
print(len(set(ans)))