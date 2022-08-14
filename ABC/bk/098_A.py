A, B = map(int, input().split())

ADD = A + B
SUB = A - B
MUL = A * B

print(max(ADD, SUB, MUL))