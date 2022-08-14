N = int(input())
A = 0

for i in range(1, N+1):
    A += (i * 10000)

print(A // N)