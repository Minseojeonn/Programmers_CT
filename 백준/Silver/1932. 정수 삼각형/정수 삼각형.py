num_size = int(input())
dp = []
triangle = []
for i in range(1,num_size+1):
    dp.append([0] * i)
    
for i in range(num_size):
    triangle.append(list(map(int, input().split(" "))))

#choose = down, down right
for i in range(num_size):
    for jdx, j in enumerate(triangle[i]):
        if jdx == 0:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        elif jdx == len(triangle[i])-1:
            dp[i][jdx] = dp[i-1][-1] + triangle[i][jdx]
        else:
            dp[i][jdx] = max(dp[i-1][jdx] + triangle[i][jdx], dp[i-1][jdx-1] + triangle[i][jdx])

print(max(dp[-1]))