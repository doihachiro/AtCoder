n = int(input())
p = list(map(int, input().split()))
count = 0

for i in range(2, n):
    if (p[i-2] < p[i-1] < p[i]) or (p[i] < p[i-1] < p[i-2]):
        count += 1

print(count)