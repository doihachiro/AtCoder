N = list(range(1,2*int(input())+2))

while N:
  print(N.pop())
  N.remove(int(input()))