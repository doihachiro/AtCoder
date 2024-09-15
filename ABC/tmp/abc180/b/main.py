N = int(input())
x = list(map(int, input().split()))

M = []
E = []
C = []

for i in range(N):
    M.append(abs(x[i]))
    E.append(abs(x[i]) ** 2)
    C.append(abs(x[i]))

print(sum(M))
print(sum(E) ** 0.5)
print(max(M))