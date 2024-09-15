N, X = map(int, input().split())
tmp = 0

for i in range(1, N+1):
    V, P = map(int, input().split())
    tmp += V * P
    if X * 100 < tmp:
        print(i)
        exit()

print(-1)