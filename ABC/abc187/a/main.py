A, B = input().split()

X = int(A[0]) + int(A[1]) + int(A[2])
Y = int(B[0]) + int(B[1]) + int(B[2])

if X > Y:
    print(X)
else:
    print(Y)