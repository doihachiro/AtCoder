A, B, C = map(int, input().split())

if A > B or (A == B and C == 1):
    print("Takahashi")
else:
    print("Aoki")