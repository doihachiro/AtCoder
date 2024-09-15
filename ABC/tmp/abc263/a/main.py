A = list(map(int, input().split()))
N = sorted(A)

if len(set(N)) == 2:
    if N[0] == N[1] and N[3] == N[4]:
        exit(print("Yes"))
print("No")