N, T = map(int, input().split())
count = 0
X = []

for i in range(N):
    X.append(int(input()))

for j in range(1, N):
    if (X[j] - X[j-1]) >= T:
        count += T
    else:
        count += (X[j] - X[j-1])

print(count + T)