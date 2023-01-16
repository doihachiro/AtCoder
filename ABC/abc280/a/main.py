H, W = map(int, input().split())
count = 0

for _ in range(H):
    tmp = input()
    count += tmp.count("#")

print(count)