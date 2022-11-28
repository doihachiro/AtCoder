N = int(input())
A = list(map(int, input().split()))
tmp = []

for i in range(N):
    tmp.append(1 / A[i])

print(1 / sum(tmp))