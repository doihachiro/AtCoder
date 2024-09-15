N = int(input())
A = list(map(int, input().split()))

ans = sorted(A)

print(A.index(ans[-2]) + 1)