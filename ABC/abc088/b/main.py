N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
A = 0
B = 0

for i in range(0, N, 2):
    A += a[i]

for j in range(1, N, 2):
    B += a[j]

print(abs(A - B))