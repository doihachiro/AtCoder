A, B, C, D, E, F, X = map(int, input().split())

t = X // (A + C) * A * B + B * min(A, X % (A + C))
a = X // (D + F) * D * E + E * min(D, X % (D + F))

if t > a :
    print("Takahashi")
elif t < a :
    print("Aoki")
else:
    print("Draw")