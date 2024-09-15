N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N-1, -1, -1):
    print("".join(S[i]))