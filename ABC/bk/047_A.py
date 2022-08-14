N = list(map(int, input().split()))
N = sorted(N)

if N[-1] == sum(N[:-1]):
    print("Yes")
else:
    print("No")