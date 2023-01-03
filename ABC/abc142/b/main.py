N, K = map(int, input().split())
h = list(map(int, input().split()))
count = 0

for i in range(N):
    if K <= h[i]:
        count += 1

print(count)