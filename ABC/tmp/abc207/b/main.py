A, B, C, D = map(int, input().split())
R = 0
count = 0

if C * D <= B:
    print(-1)
else:
    while R * D < A:
        A += B
        R += C
        count += 1
    else:
        print(count)