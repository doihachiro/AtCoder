N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        A[tmp[1] - 1] = tmp[2]
    if tmp[0] == 2:
        print(A[tmp[1] - 1])