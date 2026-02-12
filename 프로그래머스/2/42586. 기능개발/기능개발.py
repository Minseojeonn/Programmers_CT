from collections import deque
def solution(progresses, speeds):
    queue_progresses = deque(progresses)
    queue_speeds = deque(speeds)
    answer = []
    work_days = 0
    while queue_progresses:
        work_days += 1
        local_finished_works=0
        while True and queue_progresses:
            if queue_progresses[0] + queue_speeds[0] * work_days >= 100:
                queue_progresses.popleft()
                queue_speeds.popleft()
                local_finished_works += 1
            else:
                break
        if local_finished_works != 0:
            answer.append(local_finished_works)
            
    return answer