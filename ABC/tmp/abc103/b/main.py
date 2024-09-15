S = input()
N = input()

for i in range(len(S)):
    tmp = S[-1] + S[:-1]
    if tmp == N:
        print("Yes")
        exit()
    else:
        S = tmp

print("No")