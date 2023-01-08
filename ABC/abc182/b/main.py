N = int(input())
A = list(map(int, input().split()))
count = 0
max_count = 0

for i in range(2, 1001):
    count = 0
    for j in A:
        if j % i == 0:
            count += 1
    if max_count < count:
        max_count = count
        ans = i

print(ans)