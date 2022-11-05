N = int(input())
A = 1

for i in range(1, N + 1):
    A *= i
    A %= 10 ** 9 + 7

print(A)