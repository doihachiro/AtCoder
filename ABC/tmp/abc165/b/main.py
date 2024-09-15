X = int(input())
Y = 0
tmp = 100

while tmp < X:
    Y += 1
    tmp += tmp // 100

print(Y)