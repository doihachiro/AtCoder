N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
tmp = 1000

for i in range(N):
    if abs(A - (T - H[i] * 0.006)) < tmp:
        tmp = abs(A - (T - H[i] * 0.006))
        ans = i + 1

print(ans)