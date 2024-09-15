N, S, T = map(int, input().split())
count = 0

for i in range(N):
    if i == 0:
        W = int(input())
    else:
        W += int(input())

    if S <= W <= T:
        count += 1

print(count)