N = int(input())
A = list(map(int, input().split()))

S = sum(A)
P = 0

for i in range(N):
    if S >= 4:
        P += 1
        S -= A[i]
print(P)