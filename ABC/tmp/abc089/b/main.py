N = int(input())
S = list(input().split())
ans = set(S)

if len(ans) == 3:
    print("Three")
elif len(ans) == 4:
    print("Four")