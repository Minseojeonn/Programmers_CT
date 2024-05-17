import heapq
from collections import deque
def solution(jobs):
    #작업 가능한 것 중, 사용 시간이 작은 순서대로 짜른다
    len_jobs = len(jobs)
    jobs = deque(sorted(jobs))
    heap = []
    end_time = -1
    consume_time = 0
    processing = False
    for time in range(999999):
        while jobs and jobs[0][0] == time:
            input_time, processing_time = jobs.popleft()
            heapq.heappush(heap,(processing_time, input_time))
        if heap and processing == False:
            processing_time, input_time = heapq.heappop(heap)
            end_time = time+processing_time
            consume_time += end_time - input_time 
            processing = True
            #print(consume_time)
        if processing and time == end_time-1:
            processing = False
    #print(consume_time)
    if heap:
        raise "ERORR"
    return consume_time // len_jobs