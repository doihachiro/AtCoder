S = list(input())
V = list(input())
N = len(S)

if S == V:
    print("Yes")
    exit()

for i in range(N-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S == V:
        print("Yes")
        exit()
    else:
        S[i], S[i+1] = S[i+1], S[i]

print("No")