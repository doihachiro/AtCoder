import math
a, b, d = map(int, input().split())
rad_d = math.radians(d)

ans_a = a * math.cos(rad_d) - b * math.sin(rad_d)
ans_b = a * math.sin(rad_d) + b * math.cos(rad_d)

print(ans_a, ans_b)