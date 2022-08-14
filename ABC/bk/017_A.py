A = 0

for i in range(3):
    S, E = map(int, input().split())
    A += S * E // 10
print(A)