N = int(input())
S = list(input())
tmp = 0
ans = 0

for i in range(N):
    if S[i] == "I":
        tmp += 1
    elif S[i] == "D":
        tmp -= 1
    ans = max(ans, tmp)

print(ans)