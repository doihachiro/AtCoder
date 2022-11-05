w = list(input())

for i in range(97, 122):
    if w.count(chr(i)) % 2 != 0:
        print("No")
        exit()

print("Yes")