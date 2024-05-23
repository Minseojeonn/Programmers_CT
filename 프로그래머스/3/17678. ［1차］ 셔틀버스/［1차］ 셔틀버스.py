def time_converter(HHMM):
    hour, minuts = HHMM.split(":")
    return int(hour)*60+int(minuts)
def hour_converter(mins):
    return f"{(mins//60):02d}:{(mins%60):02d}"
def count_superior(time_table,pivot):
    for idx,value in enumerate(time_table):
        if value <= pivot:
            break
    return len(time_table) - idx
from collections import deque
def solution(n, t, m, timetable):
    #9:00부터 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명이 탈 수. ㅣㅆ음.
    #도착시간 포함.
    answer = 0
    first_bus = "09:00"
    waiter = deque(sorted(timetable))
    for i in range(0,n-1):
        time = hour_converter(time_converter(first_bus) + i*t)
        can_ride = m
        while True:
            if can_ride > 0 and waiter and waiter[0] <= time:
                can_ride -= 1
                waiter.popleft()
            else:
                break
    time = hour_converter(time_converter(first_bus) + (n-1)*t)
    if len(waiter) < m:
        answer = time
    else:
        can_ride = m
        while waiter:
            if waiter[0] > time:
                answer = time
                break
            if can_ride == 1:
                answer = hour_converter(time_converter(waiter[0])-1)
                break
            waiter.popleft()
            can_ride -= 1
        #print(waiter)
    return answer