from re import A


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = []

for i in range(N):
  if i != A[i] and i != B[i]:
    print("No")
    break
  else:
    X.append(i)
for j in range(N):
  if abs(X[j] - X[j+1]) >= K:
    print("No")
    break
  print("Yes")