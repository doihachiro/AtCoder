N = int(input())
T = input()

A = [0, 0, 0, 0]
C = 1

for i in range(N):
    if T[i] == "S":
        A[C] += 1 
    elif C == 3:
        C = 0
    else:
        C += 1

x = A[1] - A[3]
y = A[0] - A[2]


print(x, y)