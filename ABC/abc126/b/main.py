S = input()
A = int(S[:2])
B = int(S[2:])

if (A > 12 or A == 0) and (B <= 12 and B != 0):
    print("YYMM")
elif (B > 12 or B == 0) and (A <= 12 and A != 0):
    print("MMYY")
elif (A <= 12 and A >= 1) and (B <= 12 and B >= 1):
    print("AMBIGUOUS")
else:
    print("NA")