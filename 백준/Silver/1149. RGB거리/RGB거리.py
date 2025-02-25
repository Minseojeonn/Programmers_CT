import sys

num_house = int(sys.stdin.readline().strip())
cost = []

for _ in range(num_house):
    cost.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, num_house):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[num_house-1]))