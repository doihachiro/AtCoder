S = input() + "0"
A = ""
count = 1
now = S[0]

for i in range(1, len(S)):
    if S[i-1] == S[i]:
        count += 1
    else:
        A += now
        A += str(count)
        now = S[i]
        count = 1

print(A)