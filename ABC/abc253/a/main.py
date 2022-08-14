a, b, c = map(int, input().split())

if b <= a or b <= c:
    if b >= a or b >= c:
        print("Yes")
    else:
        print("No")
else:
    print("No")