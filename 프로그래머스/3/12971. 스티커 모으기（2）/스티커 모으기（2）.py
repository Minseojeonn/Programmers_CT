#스티커에서 몇장을 뜯어내서, 숫자의 합이 최대가 되도록 하고 싶음. 근데 뜯는순간 좌우는 사용할 수 없게됨.
#DP로 푸는 문제 같은데 ..
def DP(sentence):
    dp = [0 for i in range(len(sentence))]
    for idx in range(len(sentence)):
        if idx == 0:
            dp[0] = sentence[0]
        elif idx == 1:
            dp[idx] = max(dp[0], sentence[idx])
        else:
            dp[idx] = max(dp[idx-1], sentence[idx] + dp[idx-2])
    return dp[-1]

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    DP1 = DP(sticker[:-1])
    DP2 = DP(sticker[1:])
    return max(DP1, DP2)