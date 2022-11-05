A = list(input())
B = list(input())
C = list(input())
X = A.pop(0)

while True:
    if X == "a":
        if len(A) == 0:
            print("A")
            break
        X = A.pop(0)

    if X == "b":
        if len(B) == 0:
            print("B")
            break
        X = B.pop(0)

    if X == "c":
        if len(C) == 0:
            print("C")
            break
        X = C.pop(0)