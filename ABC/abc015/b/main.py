from math import ceil, floor

N = int(input())
tmp = list(map(int, input().split()))
A = 0

for i in range(N):
    if tmp[i] == 0:
        N -= 1
    A += tmp[i]

print(ceil(A / N))