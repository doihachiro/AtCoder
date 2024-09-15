N = int(input())
S = input()
tmp = N // 2


if N % 2 == 0 and S[0:tmp] == S[tmp:N]:
    print("Yes")
else:
    print("No")