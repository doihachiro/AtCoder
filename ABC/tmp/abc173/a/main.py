N = int(input())
X = N // 1000

if N % 1000 == 0:
    print(0)
else:
    print(1000 * (X + 1) - N)