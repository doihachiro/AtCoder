import math
N = int(input())
R = []

for i in range(N):
    R.append(int(input()))

R.sort(reverse=True)
ans = R[0] ** 2

for i in range(1, N):
    if i % 2 != 0:
        ans -= R[i] ** 2
    elif i % 2 == 0:
        ans += R[i] ** 2

print(ans * math.pi)