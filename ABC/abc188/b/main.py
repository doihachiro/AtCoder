N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = 0

for i, j in zip(A, B):
    X += i * j

if X == 0:
    print("Yes")
else:
    print("No")