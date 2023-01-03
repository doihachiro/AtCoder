N = int(input())
S = list(input())
ans = []

for i in range(len(S)):
    tmp = ord(S[i]) + N
    if 90 < tmp:
        tmp -= 26
    ans += chr(tmp)

print("".join(ans))