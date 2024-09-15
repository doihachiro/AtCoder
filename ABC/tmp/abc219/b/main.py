S = []
ans = ""
for _ in range(3):
    S.append(input())

T = list(map(int, (input())))

for i in T:
    ans += S[i-1]

print(ans)