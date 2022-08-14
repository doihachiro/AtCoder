A = int(input())
B = int(input())

N = A % B
if N == 0:
    print(N)
else:
    print(B - N)