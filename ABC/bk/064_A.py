r, g, b = input().split()

N = r + g + b

if int(N) % 4 == 0:
    print("YES")
else:
    print("NO")