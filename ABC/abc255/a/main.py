R, C = map(int, input().split())
a11, a12 = map(int, input().split())
a21, a22 = map(int, input().split())

s = [[a11, a12],[a21, a22]]
print(s[R-1][C-1])