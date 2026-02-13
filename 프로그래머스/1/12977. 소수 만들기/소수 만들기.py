from itertools import combinations
def solution(nums):
    answer = 0
    def checker(sum_picked):
        for i in range(2, sum_picked):
            if sum_picked % i == 0:
                return False
        return True
    
    for picked in combinations(nums, 3):
        if checker(sum(picked)):
            answer += 1
    
    return answer