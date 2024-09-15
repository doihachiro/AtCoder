a, b, c, d = map(int, input().split())

if (abs(a - b) <= d >= abs(b - c)) or (abs(a - c) <= d):
    print("Yes")
else:
    print("No")