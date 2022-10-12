S = input()
T = input()
X = "atcoder"

for s, t in zip(S, T):
    if (s == t) or (s == "@" and t in X) or (s in X and t == "@"):
         continue
    else:
        print("You will lose")
        exit()

print("You can win")