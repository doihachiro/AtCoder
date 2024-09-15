N = int(input())
AC  = 0
WA  = 0
TLE = 0
RE  = 0

for _ in range(N):
    tmp = input()
    if tmp == "AC":
        AC += 1
    elif tmp == "WA":
        WA += 1
    elif tmp == "TLE":
        TLE += 1
    elif tmp == "RE":
        RE += 1

print("AC x " + str(AC))
print("WA x " + str(WA))
print("TLE x " + str(TLE))
print("RE x " + str(RE))