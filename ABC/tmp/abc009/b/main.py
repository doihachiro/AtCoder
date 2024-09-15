N = int(input())
A = set()

for _ in range(N):
    A.add(int(input()))

L = list(A)
L.sort()
print(L[-2])