import re
S = input()

if len(S) == len(set(S)) and re.search("[A-Z]", S) and re.search("[a-z]", S):
    print("Yes")
else:
    print("No")