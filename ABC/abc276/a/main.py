S = input()
ans = 0

for i in range(len(S)):
    if S[i] == "a":
        ans = i + 1

if ans != 0:
    print(ans)
else:
    print(-1)