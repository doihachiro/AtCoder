W = input()
a = ""

for i in W:
    if i not in ["a", "i", "u", "e", "o"]:
        a += i
print(a)