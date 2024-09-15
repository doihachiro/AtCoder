N = input()
A = []

for i in range(3):
    if N[i] == "1":
       A.append("9")
    else:
        A.append("1")

print(A[0] + A[1] + A[2])