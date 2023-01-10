S = input()
X = []

for i in S:
    if i == "6":
        X.append("9")
    elif i == "9":
        X.append("6")
    else:
        X.append(i)

print("".join(reversed(X)))
