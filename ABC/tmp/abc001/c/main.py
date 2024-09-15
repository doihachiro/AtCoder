Deg, Dis = map(int, input().split())

if 112.5 <= Deg < 337.5:
    Dir = "NNE"
elif 337.5 <= Deg < 562.5:
    Dir = "NE"
elif 562.5 <= Deg < 787.5:
    Dir = "ENE"
elif 787.5 <= Deg < 1012.5:
    Dir = "E"
elif 1012.5 <= Deg < 1237.5:
    Dir = "ESE"
elif 1237.5 <= Deg < 1462.5:
    Dir = "SE"
elif 1462.5 <= Deg < 1687.5:
    Dir = "SSE"
elif 1687.5 <= Deg < 1912.5:
    Dir = "S"
elif 1912.5 <= Deg < 2137.5:
    Dir = "SSW"
elif 2137.5 <= Deg < 2362.5:
    Dir = "SW"
elif 2362.5 <= Deg < 2587.5:
    Dir = "WSW"
elif 2587.5 <= Deg < 2812.5:
    Dir = "W"
elif 2812.5 <= Deg < 3037.5:
    Dir = "WNW"
elif 3037.5 <= Deg < 3262.5:
    Dir = "NW"
elif 3262.5 <= Deg < 3487.5:
    Dir = "NNW"
else:
    Dir = "N"

Dis = ((Dis / 60) * (10 ** 1) * 2 + 1) // 2 / (10 ** 1)
if 0.0 <= Dis <= 0.2:
    Dir = "C"
    W = 0
elif 0.3 <= Dis <= 1.5:
    W = 1
elif 1.6 <= Dis <= 3.3:
    W = 2
elif 3.4 <= Dis <= 5.4:
    W = 3
elif 5.5 <= Dis <= 7.9:
    W = 4
elif 8.0 <= Dis <= 10.7:
    W = 5
elif 10.8 <= Dis <= 13.8:
    W = 6
elif 13.9 <= Dis <= 17.1:
    W = 7
elif 17.2 <= Dis <= 20.7:
    W = 8
elif 20.8 <= Dis <= 24.4:
    W = 9
elif 24.5 <= Dis <= 28.4:
    W = 10
elif 28.5 <= Dis <= 32.6:
    W = 11
elif 32.7 <= Dis:
    W = 12

print(Dir + " " + str(W))