A, B, W = map(int, input().split())
MAX = 0
MIN = 10 ** 6 + 1

for i in range(1, (10 ** 6 + 1)):
    if (A * i) <= (W * 1000) <= (B * i):
        MAX = max(MAX, i)
        MIN = min(MIN, i)

if MAX == 0:
    print("UNSATISFIABLE")
else:
    print(str(MIN) + " " + str(MAX))