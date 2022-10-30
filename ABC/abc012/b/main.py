N = int(input())
print("{:02}:{:02}:{:02}".format(N // 3600, N // 60 % 60, N % 60))
