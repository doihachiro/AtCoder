N, K, Q = map(int,input().split())
A = list(map(int,input().split())) + [N+1]
L = list(map(int,input().split()))

for l in L:
  l -= 1
  if A[l+1] - A[l] != 1:
    A[l] += 1
    
print(*A[:-1])