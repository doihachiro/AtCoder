S = input()
ans = 1000000000

for i in range(2, len(S)):
    ans = min(ans, abs(753 - int(S[i-2] + S[i-1] + S[i])))

print(ans)