A, B = (input().split()) 

if A == "H":
    print(B)
elif A == "D":
    if B == "H":
        print("D")
    else:
        print("H")