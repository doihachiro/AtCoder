N = int(input())
s = []
p = []

for i in range(N):
    S, P = (input().split())
    s.append(S)
    p.append(int(P))

sum = sum(p)

for j in range(N):
    if sum / 2 < p[j]:
        print(s[j])
        exit()

print("atcoder")