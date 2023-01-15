AB = []
CD = []

for i in range(1, 11):
    tmp = list(input())
    if "#" in tmp:
        AB.append(i)
        for j in range(10):
            if tmp[j] == "#":
                CD.append(j+1)

print(min(AB), max(AB))
print(min(CD), max(CD))