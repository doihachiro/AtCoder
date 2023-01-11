N = int(input())
S = list(map(int, input()))

for i in range(N):
    if S[i] == 1:
        if (i + 1) % 2 == 0:
            print("Aoki")
        else:
            print("Takahashi")
        exit()