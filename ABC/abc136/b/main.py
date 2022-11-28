N = int(input())

if N < 10 ** 1:
    print(N)
elif N < 10 ** 2:
    print(9)
elif N < 10 ** 3:
    print(N - 90)
elif N < 10 ** 4:
    print(909)
elif N < 10 ** 5:
    print(N - 9090)
else:
    print(90909)