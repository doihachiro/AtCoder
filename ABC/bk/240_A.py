a, b = map(int, input().split())
ans = abs(a - b)

if ans == 1 or ans == 9:
    print("Yes")
else:
    print("No")