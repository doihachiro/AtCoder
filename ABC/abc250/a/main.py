H, W = map(int, input().split())
R, C = map(int, input().split())

A = 0

if R + 1 <= H:
    A += 1
if R - 1 >= 1:
    A += 1
if C + 1 <= W:
    A += 1
if C - 1 >= 1:
    A += 1
 
print(A)