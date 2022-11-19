N, X = map(int, input().split())
min_m = 1000
count = 0

for i in range(N):
    tmp = int(input())
    X -= tmp
    min_m = min(min_m, tmp)
    count += 1

print(count + (X // min_m))