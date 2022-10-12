M = int(input())
m = M / 1000

if m < 0.1:
    print("00")
elif 0.1 <= m and m <= 5:
    if (m * 10) < 10:
        print("0" + str(int(m * 10)))
    else:
        print(int(m * 10))
elif 6 <= m and m <= 30:
    print(int(m + 50))
elif 35 <= m and m <= 70:
    print(int(74 + m / 5))
elif 70 < m:
    print(89)