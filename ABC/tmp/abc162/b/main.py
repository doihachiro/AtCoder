N = list(range(1, int(input()) + 1))
ans = 0

for i in N:
    if (i % 3 != 0) and (i % 5 != 0):
        ans += i

print(ans)