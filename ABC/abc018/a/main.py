A = [int(input()) for i in range(3)]
B = sorted(A, reverse = 1)
 
for i in A:
  print(B.index(i) + 1)