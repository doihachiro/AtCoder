H, W = map(int, input().split())
A = []

for i in range(H):
    A.append(input())

print(("#" * W) + "##")
for j in range(H):
    print("#" + A[j] + "#")
print(("#" * W) + "##")