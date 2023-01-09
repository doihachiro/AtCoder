N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MAX = max(A)
MIN = min(B)

print(max(0, MIN - MAX + 1))