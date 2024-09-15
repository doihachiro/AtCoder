S = input()
N = len(S)

if S != S[N::-1]:
    print("No")
    exit()

tmp = S[:(N-1)//2]
if tmp != tmp[len(tmp)::-1]:
    print("No")
    exit()

tmp = S[(N+2)//2:]
if tmp != tmp[len(tmp)::-1]:
    print("No")
    exit()

print("Yes")