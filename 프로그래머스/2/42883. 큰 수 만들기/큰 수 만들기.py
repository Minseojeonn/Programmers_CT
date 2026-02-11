from collections import deque
def solution(number, k):
    number_list = [number[0]]
    remain_k = k
    for num in deque(number[1:]):
        while len(number_list) > 0 and number_list[-1] < num and remain_k != 0:
            number_list.pop()
            remain_k -= 1
        number_list.append(num)
    if remain_k > 0:
        number_list = number_list[:-remain_k]
    
    return "".join(number_list)