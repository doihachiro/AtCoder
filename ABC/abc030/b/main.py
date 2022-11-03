n, m = map(int, input().split())

N = (n % 12) * 30 + (m * 0.5) 
M = m * 6

print(min(abs(N - M), 360 - abs(N - M)))