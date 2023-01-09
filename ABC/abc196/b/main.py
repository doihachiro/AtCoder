W = input()
X = W.find(".")

if X != -1:
    print(W[:X])
else:
    print(W)