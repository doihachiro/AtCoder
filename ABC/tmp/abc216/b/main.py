N = int(input())
ans = []

for _ in range(N):
    ans.append(tuple(input().split())) 

if len(ans) != len(set(ans)):
    print("Yes")
else:
    print("No")