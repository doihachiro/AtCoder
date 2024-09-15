s = input()
A = []

for i in range(len(s)):
    if s[i] == "0" or s[i] == "1":
        A.append(s[i])
    elif len(A) > 0 and s[i] == "B":
        A.pop()

print("".join(A))