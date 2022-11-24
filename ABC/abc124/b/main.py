N = int(input())
H = list(map(int, input().split()))
A = H[0]
count = 1

for i in range(1, N):
    if A <= H[i]:
        count += 1
        A = H[i]

print(count)