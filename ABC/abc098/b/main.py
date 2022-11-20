N = int(input())
S = input()
ans = 0

for i in range(N):
    A = set(S[:i])
    B = set(S[i:])
    ans = max(ans, len(A & B))

print(ans)