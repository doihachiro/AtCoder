A = list(map(int, input().split()))
A.sort()
print(A[2]*10 + A[0] + A[1])