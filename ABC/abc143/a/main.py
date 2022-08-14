A, B = map(int, input().split())

if A > B:
    if 0 <= (A - (2 * B)):
        print(A - (2 * B))
    else:
        print(0)
else:
    print(0)