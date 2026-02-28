#계단 오르기
#계단 한번에 1개 or 2개씩, 연속 3개 X, 마지막 밟아야함
# DP 문제? 개단 개수 300개 이하니까 dp로 풀릴듯?

num_stairs = int(input())
stair_costs = []
dp = [0] * (num_stairs)

for i in range(num_stairs):
    stair_costs.append(int(input()))

dp[0] = stair_costs[0]
for i in range(1, num_stairs):
    if i == 1:
        dp[1] = stair_costs[1] + stair_costs[0]
    elif i == 2:
        dp[2] = max(stair_costs[0] + stair_costs[2], stair_costs[2] + stair_costs[1])
    else:
        dp[i] = max(stair_costs[i] + stair_costs[i-1] + dp[i-3], dp[i-2] + stair_costs[i])

print(dp[-1])