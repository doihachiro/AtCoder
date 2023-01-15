N, W = map(int, input().split())
A = [0 , 0] + list(map(int,input().split()))
ans = set()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        for k in range(j+1, len(A)):
            if A[i] + A[j] + A[k] <= W:
                ans.add(A[i] + A[j] + A[k])

print(len(ans))