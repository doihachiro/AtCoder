import re
S = input()
tmp = re.compile("\A[A-Z][1-9]\d{5}[A-Z]\Z")

if tmp.match(S):
    print("Yes")
else:
    print("No")