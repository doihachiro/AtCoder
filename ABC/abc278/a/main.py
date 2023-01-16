N, K = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(K):
    A.append(0)

print(*A[K:N+K])