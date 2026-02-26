num_items, indure_weight = map(int,input().split(" "))
dp = [0] * (indure_weight + 1)

items = []
for i in range(num_items):
    weight, value = map(int,input().split(" "))
    items.append((weight, value))

for weight, value in items:
    for i in range(indure_weight, weight-1, -1):
        if weight <= i:
            dp[i] = max(dp[i-weight] + value, dp[i])

print(max(dp))
        