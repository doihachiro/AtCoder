s = list(input())

A = s.index("A")
s.reverse()
Z = s.index("Z")

print(len(s) - A - Z)