N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in A:
    if 10 < i:
        ans += i - 10

print(ans)