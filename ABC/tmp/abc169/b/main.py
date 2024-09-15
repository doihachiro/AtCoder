N = int(input())
A = list(map(int, input().split()))
ans = 1

if 0 in A:
    print(0)
    exit()

for i in A:
    ans *= i
    if 10 ** 18 < ans:
        print(-1)
        exit()

print(ans)