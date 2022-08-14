N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = "Yes"

for i in range(M):
    if B[i] not in A:
        ans = "No"
        exit
    else:
        A.remove(B[i])

print(ans)