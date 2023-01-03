S = input()
X = "".join(list(reversed(S)))
count = 0

for i in range(len(S)):
    if S[i] != X[i]:
        count += 1

print(count // 2)