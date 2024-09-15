X = []
Y = [0]

for _ in range(5):
    tmp = int(input())
    X.append(tmp)
    if tmp % 10 != 0:
        Y.append(10 - (tmp % 10))

print(sum(X) + sum(Y) - max(Y))