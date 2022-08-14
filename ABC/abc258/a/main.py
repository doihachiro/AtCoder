K = int(input())

if K >= 60:
    print("22:" + str(K - 60).zfill(2))
else:
    print("21:" + str(K).zfill(2))