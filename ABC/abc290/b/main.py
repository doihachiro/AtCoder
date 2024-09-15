N, K = map(int, input().split())
S = input()
tmp = 0
count = 0

for i in S:
    count += 1 
    if i == "o":
        tmp += 1
        if tmp == K:
            break

X = "x" * (N - count)

print(S[:count] + X)