import sys
n = int(sys.stdin.readline())

# dp[i]는 i를 1로 만드는 최소 횟수
dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 1. 일단 1을 빼는 경우 (가장 기본)
    dp[i] = dp[i - 1] + 1
    
    # 2. 2로 나누어 떨어지면, 2로 나눈 경우와 비교해서 최솟값 갱신
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # 3. 3으로 나누어 떨어지면, 3으로 나눈 경우와 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])