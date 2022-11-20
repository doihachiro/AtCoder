N = input()
A = int(N)
X = 0

for i in N:
    X += int(i)

if A % X == 0:
    print("Yes")
else:
    print("No")