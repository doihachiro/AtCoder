X = input()
A = X.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")

if len(A) == 0:
    print("YES")
else:
    print("NO")