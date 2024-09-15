N = int(input())
H = (format(N, "x")).upper()

if len(H) == 1:
    print("0" + H)
else:
    print(H)