N, M, T = map(int, input().split())
power = N
tmp = 0

for i in range(M):
    A, B = map(int, input().split())
    power = power - (A - tmp)
    if power <= 0:
        print("No")
        exit()
    power += B - A
    if N < power:
        power = N
    tmp = B

if power - (T - B) <= 0:
    print("No")
else:
    print("Yes")