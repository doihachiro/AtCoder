N, X = map(int, input().split())
A = list(map(int, input().split()))
tmp = 0

for i in range(N):
    if (i + 1) % 2 == 0:
        A[i] -= 1
    tmp += A[i]

if tmp <= X:
    print("Yes")
else:
    print("No")