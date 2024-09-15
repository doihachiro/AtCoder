S = input()
a, b = map(int, input().split())

S = list(S)

tmp = S[a-1]
S[a-1] = S[b-1]
S[b-1] = tmp

print("".join(S))