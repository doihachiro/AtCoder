import collections

N = map(int, input().split())
A = list(map(int, input().split()))

C = collections.Counter(A)
print(C.most_common()[-1][0])