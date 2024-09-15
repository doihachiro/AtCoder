A, B, K = map(int, input().split())
N = A
count = 0

while A < B:
    A *= K
    count += 1

print(count)