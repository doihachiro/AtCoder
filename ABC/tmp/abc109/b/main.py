N = int(input())
A = []

for _ in range(N):
    A.append(input())

for i in range(1, N):
    if A[i-1][-1] != A[i][0]:
        print("No")
        exit()

if len(set(A)) != N:
    print("No")
    exit()

print("Yes")