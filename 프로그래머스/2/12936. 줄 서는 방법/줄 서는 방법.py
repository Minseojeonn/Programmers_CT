import math
def solution(n, k):
    candidate_list = []
    answer = []
    for i in range(1,n+1):
        candidate_list.append(i)
    
    while candidate_list:
        n = len(candidate_list)
        if n == 1:
            answer.append(candidate_list[0])
            break

        block_size = math.factorial(n - 1)          # (n-1)!
        idx = (k - 1) // block_size                 # 0-index
        answer.append(candidate_list.pop(idx))
        k = (k - 1) % block_size + 1                # 다음 단계 k (1-index 유지)
   
    return answer