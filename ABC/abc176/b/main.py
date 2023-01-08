N = input()
tmp = []

for i in N:
    tmp.append(int(i))

if sum(tmp) % 9 == 0:
    print("Yes")
else:
    print("No")