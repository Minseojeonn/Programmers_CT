#반환할 수 있는 경우의 수 
def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for coin in money:
        for i in range(coin,n+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    return dp[n]