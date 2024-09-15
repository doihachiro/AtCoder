L, R = map(int, input().split())
S = list(input())

A = S[:(L-1)]
A += reversed(S[L-1:R])
A += S[R:]

print("".join(A))