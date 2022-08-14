from statistics import mode

N = int(input())
S = []
for i in range(N):
    S.append(input())

print(mode(S))