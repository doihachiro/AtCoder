A, B, K = map(int, input().split())

if A >= K:
    print(str(A - K), str(B))
elif B >= (K - A):
    print(str(0), str(B - (K - A)))
else:
    print(str(0), str(0))