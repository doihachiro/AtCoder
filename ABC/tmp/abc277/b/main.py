N = int(input())
S = [input() for _ in range(N)]
S_tmp = tuple(S)

if len(S) != len(set(S_tmp)):
    print("No")
    exit()
else:
    for i in range(N):
        if S[i][0] not in "HDCS" or S[i][1] not in "A23456789TJQK":
            print("No")
            exit()

print("Yes")