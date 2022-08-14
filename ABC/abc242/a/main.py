A, B, C, X = map(int, input().split())
N = B - A

if A >= X:
    print(1)
elif B >= X: 
    print(C / N)
else:
    print(0)