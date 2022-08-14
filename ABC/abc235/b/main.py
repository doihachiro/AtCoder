N = map(int, input().split())
A = list(map(int, input().split()))

S = A[0]

for i in A[1:]:
    if S >= i:
        break
    S = i

print(S)