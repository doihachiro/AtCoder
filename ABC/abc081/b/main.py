N = int(input())
A = list(map(int, input().split()))
count = [1] * N

for i in range(N):
    if A[i] % 2 != 0:
        print(0)
        exit()

    while 0 < A[i]:
        A[i] /= 2
        if A[i] % 2 != 0:
            break
        else:
            count[i] += 1

print(min(count))