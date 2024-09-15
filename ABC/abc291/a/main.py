S = input()
ans = 0

for i in range(len(S)):
    if S[i].isupper() == True:
        ans = i
        break

print(ans + 1)