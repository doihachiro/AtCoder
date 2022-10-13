N = int(input())
A = list(map(int, input().split()))
c = 0

for i in range(N):
    while (A[i] % 2 == 0) or A[i] in [2, 5, 8]:
        c += 1
        A[i] -= 1 

print(c)