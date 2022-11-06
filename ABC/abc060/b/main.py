A, B, C = map(int, input().split())
c = 1

while (A * c) < 10 ** 5:
    if (A * c) % B == C:
        print("YES")
        exit()
    else:
        c += 1

print("NO")