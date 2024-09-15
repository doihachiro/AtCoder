from collections import Counter

N = int(input())
X = []

for _ in range(N):
    X.append(input())

A = Counter(X)
print(A.most_common(1)[0][0])