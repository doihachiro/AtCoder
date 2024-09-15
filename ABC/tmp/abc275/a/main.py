N = int(input())
H = list(map(int, input().split()))
ans = max(H)

print(H.index(ans) + 1)