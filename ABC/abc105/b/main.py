N = int(input())
count = 0

for i in range(101):
    for j in range(101):
        if N == i * 4 + j * 7:
            print("Yes")
            exit()

print("No")