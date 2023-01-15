S = input()
T = input()


if len(T) < len(S):
    print("No")
    exit()
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            exit()
            
print("Yes")
