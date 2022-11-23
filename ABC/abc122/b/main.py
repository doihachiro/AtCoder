S = input()
count = 0
ans = 0

for i in S:
    if i in ("A", "C", "G", "T"):
        count += 1
    else:
        ans = max(ans, count)
        count = 0

ans = max(ans, count)
print(ans)