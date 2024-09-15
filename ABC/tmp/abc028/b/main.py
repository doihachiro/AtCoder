S = list(input())
count = [0] * 6

for i in range(len(S)):
    if S[i] == "A":
        count[0] += 1
    elif S[i] == "B":
        count[1] += 1
    elif S[i] == "C":
        count[2] += 1
    elif S[i] == "D":
        count[3] += 1
    elif S[i] == "E":
        count[4] += 1
    elif S[i] == "F":
        count[5] += 1

print(*count)