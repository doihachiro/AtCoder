N, L = map(int, input().split())
A = []

for _ in range(N):
    A.append(input())

print("".join(sorted(A)))