V, A, B, C = map(int, input().split())

while True:
    if V >= A:
        V = V - A
    else:
        print("F")
        exit()
    
    if V >= B:
        V = V - B
    else:
        print("M")
        exit()
    
    if V >= C:
        V = V - C
    else:
        print("T")
        exit()