A, B, C, D = map(int, input().split())

if C > B or A > D:
    print(0)
else:
    print(abs(max(A, C) - min(B, D)))