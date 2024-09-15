N, X = map(int, input().split())
A = list(map(int, input().split()))
count = [0] * N

while True:
    if count[X-1] == 1:
        print(sum(count))
        exit()
    count[X-1] = 1
    X = A[X-1]