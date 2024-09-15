S = list(input())
ans = []

for i in range(len(S)):
    tmp = S[0]
    del S[0]
    S.append(tmp)
    ans.append("".join(S))

ans.sort()

print(ans[0])
print(ans[-1])