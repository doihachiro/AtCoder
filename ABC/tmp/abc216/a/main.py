X, Y = input().split(".")


if 0 <= int(Y) and int(Y) <= 2:
    print(X + "-")
elif 3 <= int(Y) and int(Y) <= 6:
    print(X)
else:
    print(X + "+")