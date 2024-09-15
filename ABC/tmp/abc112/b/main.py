N, T = map(int, input().split())
cost_ans = 1001
time_ans = False

for i in range(N):
    cost_tmp, time_tmp = map(int, input().split())
    if time_tmp <= T:
        cost_ans = min(cost_ans, cost_tmp)
        time_ans = True

if time_ans == False:
    print("TLE")
else:
    print(cost_ans)