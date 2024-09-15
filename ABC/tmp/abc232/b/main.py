def diff(S, T):
    return ord(S) - ord(T) if ord(S) > ord(T) else ord(S) - ord(T) + 26

S = list(input())
T = list(input())
K = diff(S[0], T[0])

for i in range(len(S)):
    if diff(S[i], T[i]) != K:
        print("No")
        exit()
print("Yes")