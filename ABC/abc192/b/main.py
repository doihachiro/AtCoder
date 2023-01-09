S = input()

for i in range(1, len(S)+1):
    if (i % 2 != 0 and S[i-1].isupper()) or (i % 2 == 0 and S[i-1].islower()):
        print("No")
        exit()

print("Yes")