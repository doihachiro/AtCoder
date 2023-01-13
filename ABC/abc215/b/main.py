N = int(input())
K = 0

while (2 ** K) <= N:
    K += 1

print(K - 1)