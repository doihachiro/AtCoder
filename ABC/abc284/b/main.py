T = int(input())

for _ in range(T):
    count = 0
    N = input()
    A = list(map(int, input().split()))
    for i in range(len(A)):
        if A[i] % 2 == 1:
            count += 1
    print(count)