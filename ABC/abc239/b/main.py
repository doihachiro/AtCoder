N = int(input())

if N >= 0:
    print(round(N // 10))
else:
    print(round(-abs(N) // 10))