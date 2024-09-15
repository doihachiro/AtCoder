S, T, X = map(int, input().split())

if X >= S and X < T:
    print("Yes")
elif S > T and X >= S:
    print("Yes")
elif S > T and X < T:
    print("Yes")
else:
    print("No")