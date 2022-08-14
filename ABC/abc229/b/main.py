A, B = list(input().split())

for i in range(min(len(A), len(B))):
    if 10 <= int(A[-1-i]) + int(B[-1-i]):
        print("Hard")
        exit()

print("Easy")