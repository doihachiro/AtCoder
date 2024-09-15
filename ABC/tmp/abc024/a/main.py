A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
N = 0

child = A * S
adult = B * T

if S + T >= K:
    N = C * (S + T)

print(child + adult - N)