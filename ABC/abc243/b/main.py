N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = 0
y = 0

for i in range(N):
    if A[i] == B [i]:
        x += 1
    
for i in range(N):
    for j in range(N):
        if (A[i] == B[j]) and (i != j):
            y += 1

print(x)
print(y)