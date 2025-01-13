n=int(input())

dp=[0,1,1,1] # n을 만들 수 있는 최소 가지수

if n >= 4:
    for i in range(4,n+1):
        # 각 케이스를 구한 후, 가장 작은 것을 선택함 -> dp에 추가를 한다.
        val1 = 1 + dp[i-1]
        val2 = 1 + dp[i-1]
        val3 = 1 + dp[i-1]

        if i%3==0:
            val1 = 1 + dp[i//3]
        if i%2==0:
            val2 = 1 + dp[i//2]
       
        dp.append(min(val1,val2,val3))
if n == 1:
    print(0)
else:
    print(dp[n])