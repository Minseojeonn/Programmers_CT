import heapq
def solution(scoville, K):
    s_queue = []
    for sco in scoville:
        heapq.heappush(s_queue, sco)
    counter = 0
    while True:
        if len(s_queue) == 1:
            if s_queue[0] >= K:
                break
            else: return -1
        if s_queue[0] >= K:
            break
        else:
            counter += 1
            cand1, cand2 = heapq.heappop(s_queue), heapq.heappop(s_queue)
            heapq.heappush(s_queue, cand1 + cand2*2)
            
    return counter