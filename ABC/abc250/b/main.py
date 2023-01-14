N, A, B = map(int, input().split())
ans1 = []
ans2 = []
count1 = 0
count2 = 0

while len(ans1) < N * B:
    for i in range(B):
        if len(ans1) == N * B:
            break
        ans1.append(".")

    for j in range(B):
        if len(ans1) == N * B:
            break
        ans1.append("#")

while len(ans2) < N * B:
    for i in range(B):
        if len(ans2) == N * B:
            break
        ans2.append("#")

    for j in range(B):
        if len(ans2) == N * B:
            break
        ans2.append(".")

ans = ans1
while count2 < N * A:
    print("".join(ans))
    count1 += 1
    count2 += 1
    if ans == ans1 and count1 == A:
        count1 = 0
        ans = ans2
    if ans == ans2 and count1 == A:
        count1 = 0
        ans = ans1