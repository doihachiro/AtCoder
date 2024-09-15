N, M, T= map(int, input().split())
A = list(map(int, input().split()))

for i in range(M):
    X, Y = map(int, input().split())
    A[X-1] -= Y

for j in range(N-1):
    T -= A[j]
    if T <= 0:
        print("No")
        exit()

print("Yes")